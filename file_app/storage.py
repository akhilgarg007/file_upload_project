from django.conf import settings
from djongo.storage import GridFSStorage


grid_fs_storage = GridFSStorage(
    collection='myfiles', base_url=''.join([settings.BASE_URL, 'api/myfiles/'])
)
