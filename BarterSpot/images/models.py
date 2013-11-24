from django.db import models
from PIL import Image
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from BarterSpot.utils.constants import MIN_SMALL_X, MIN_SMALL_Y


class BarterImage(models.Model):
    small_img = models.ImageField(upload_to='images/')
    normal_img = models.ImageField(upload_to='images/')

    @staticmethod
    def imageFromUpload(img):
        print(img._get_name())
        newImage = BarterImage.objects.create()
        newImage.normal_img = img
        temp_image_file = StringIO.StringIO(img.read())
        smallImage = Image.open(temp_image_file)
        smallImage.thumbnail((MIN_SMALL_X, MIN_SMALL_Y), Image.ANTIALIAS)
        tempfile_io = StringIO.StringIO()
        smallImage.save(tempfile_io, format='JPEG')
        smallImageName = 'small_' + img._get_name()
        newImage.small_img = InMemoryUploadedFile(tempfile_io,
                                                  None,
                                                  smallImageName,
                                                  'image/jpeg',
                                                  tempfile_io.len,
                                                  None)
        newImage.save()
        return newImage
