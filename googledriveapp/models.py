from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Folder(models.Model):
    foldername = models.CharField(max_length=50)
    folderdesc = models.CharField(max_length=255)
    folderuser = models.ForeignKey(User,on_delete=models.CASCADE)
class File(models.Model):
    filetitle = models.CharField(max_length=50)
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to="Files")