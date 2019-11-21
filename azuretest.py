

from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
import picamera

camera = picamera.PiCamera()
camera.capture('image1.jpg')

block_blob_service = BlockBlobService(account_name='kcamera', account_key='5TqWMYA/fuCZqO6IGg0crR7AZV25BS9rnszca40pQxGgqKm0U7LaOxQ2b/09tAAda5KPMUFCDFFuKEAhcI8QXg==')

block_blob_service.create_blob_from_path(
    'minor',
    'firstblood.jpg',
    'image1.jpg',
    content_settings=ContentSettings(content_type='image/jpeg'))
