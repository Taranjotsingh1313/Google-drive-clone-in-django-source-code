from django.contrib import admin
from googledriveapp.models import File, Folder
# Register your models here.
@admin.register(Folder)
class Adminfolder(admin.ModelAdmin):
   list_display = ('foldername','folderuser')
   
@admin.register(File)
class Adminfolder(admin.ModelAdmin):
   list_display = ('id','file','filetitle')