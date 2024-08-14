from rest_framework import serializers
from file_app.models import File


class FileSerializer(serializers.ModelSerializer):
    """
    Serializer for the File model.
    """
    class Meta:
        model = File
        fields = ('id', 'file_name', 'file_summary')
