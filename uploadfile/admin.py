from django.contrib import admin
# from mysite import models

from uploadfile import models
# from mysite import models
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display=('docfile','upload_date') 
    search_fields=('docfile','upload_date') 


admin.site.register(models.Document, DocumentAdmin)

