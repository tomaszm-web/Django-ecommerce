import os
import random
from django.db import models

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3989545343)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
# FileField was changed to ImageField because we want to only allow image files

    def __str__(self):
        return self.title

