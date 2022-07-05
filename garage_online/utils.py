import os

from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def refactor_image(image, band_name, band_id):
    # Open the image using Pillow
    img = Image.open(image)
    # Determine new width
    new_width = 760
    # check if either the width or height is greater than the max
    if img.width > new_width:
        output_size = (new_width, int(new_width * img.height / img.width))
        # Create a new resized “thumbnail” version of the image with Pillow
        img.thumbnail(output_size)
        # Find the file name of the image
        # img_filename = Path(image.file.name).name
        # Spilt the filename on “.” to get the file extension only
        img_suffix = Path(image.file.name).name.split(".")[-1].lower()
        # Use the file extension to determine the file type from the image_types dictionary
        img_format = image_types[img_suffix]
        # New filename
        img_new_filename = f'{band_name}_{band_id}.{img_suffix}'
        # Save the resized image into the buffer, noting the correct file type
        buffer = BytesIO()
        img.save(buffer, format=img_format)
        # Wrap the buffer in File object
        file_object = File(buffer)
        # Save the new resized file as usual, which will save to S3 using django-storages
        image.save(img_new_filename, file_object)


def refactor_song_dir(instance, filename):
    return f'songs/{instance.band.id}_{instance.band.name}_-_{filename}'

