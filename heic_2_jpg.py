from PIL import Image
from pillow_heif import register_heif_opener
import os
register_heif_opener()



# Open HEIF or HEIC file
image = Image.open('example.heic')

# Convert to JPEG
image.convert('RGB').save('example.jpg')
