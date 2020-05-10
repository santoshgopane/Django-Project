from django.db import models

# Create your models here.

class blogging(models.Model):
    # id : int Id will automatically created!
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='all_pics')
    desc = models.CharField(max_length=100)
