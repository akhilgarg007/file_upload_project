from django.http import FileResponse
from rest_framework import viewsets, status, generics, renderers, response

from file_app.models import File
from file_app.serializers import FileSerializer
from file_app.storage import grid_fs_storage
from file_app.utils import get_file_summary


class FileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing file instances.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle file uploads and save file metadata in the database.
        """
        file = request.FILES['file']
        if file.name.split('.')[-1] not in ['docx', 'pptx', 'pdf']:
            return response.Response({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)
        if File.objects.filter(file_name=file.name).exists():
            return response.Response({'error': 'File already exists'}, status=status.HTTP_400_BAD_REQUEST)
        file_summary = get_file_summary(file)
        file_instance = File(file_name=file.name, file=file)
        file_instance.file_summary = file_summary
        file_instance.save()
        return response.Response(FileSerializer(file_instance).data, status=status.HTTP_201_CREATED)


class ServeGridFSFileView(generics.GenericAPIView):
    """
    A viewset for viewing and editing file instances.
    """
    queryset = File.objects.all()
    renderer_classes = [renderers.JSONRenderer]

    def get(self, *args, **kwargs):
        """
        Get the file from database and stream it
        """
        # try:
        instance = self.get_object()
        file = instance.file
        file_handle = grid_fs_storage.open(file.name, 'rb')
        file_response = FileResponse(file_handle)
        file_response['Content-Disposition'] = f'inline; filename="{file.name}"'
        if file.size:
            file_response['Content-Length'] = file.size
        return file_response
