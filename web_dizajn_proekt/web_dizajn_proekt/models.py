from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Favourite(models.Model):
    plant_id = models.IntegerField()
    img_src = models.CharField(max_length=255)
    plant_name = models.CharField(max_length=255)
    latin_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.plant_name +" "+ str(self.plant_id)
    