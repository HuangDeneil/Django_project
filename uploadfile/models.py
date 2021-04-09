from django.db import models
from django.utils import timezone


# Create your models here.





class Document(models.Model):
    docfile = models.FileField(upload_to='documents/upload')
    # upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)








