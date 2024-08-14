from django.urls import path, include
from rest_framework.routers import DefaultRouter
from file_app.views import FileViewSet, ServeGridFSFileView

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='file')

urlpatterns = [
    path('', include(router.urls)),
    path('myfiles/<str:pk>', ServeGridFSFileView.as_view(), name='serve_gridfs_file'),
]
