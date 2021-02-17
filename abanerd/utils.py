import hashlib
import requests
import tempfile

from .models import CEUImageFile


def checksum_factory(file, hash_factory=hashlib.md5, chunk_num_blocks=128):
    h = hash_factory()
    for chunk in file.chunks():
        h.update(chunk)
    return h.hexdigest()


def create_ceu_image_object(filename, image_url):
    r = requests.get(image_url, stream=True)
    temp_file = tempfile.TemporaryFile()

    for block in r.iter_content(1024 * 8):
        if not block:
            break
        temp_file.write(block)

    ceu_image_file_object = CEUImageFile.objects.create(filename=filename, image_url=image_url)
    ceu_image_file_object.image.save(filename, temp_file)
    ceu_image_file_object.save()

    return ceu_image_file_object


def get_or_create_ceu_image_object(image_url):
    filename = image_url.split('/')[-1]

    ceu_image = CEUImageFile.objects.filter(image_url=image_url).first()
    if ceu_image:
        return ceu_image
    else:
        return create_ceu_image_object(filename, image_url)


def parse_csv(file, provider=None):
    pass
