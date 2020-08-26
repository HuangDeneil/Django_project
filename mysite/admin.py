from django.contrib import admin
from mysite import models


# Register your models here.
class SpeciseAdmin(admin.ModelAdmin):
    list_display=('specise_name', 'pub_date')   #  要顯示的欄位
    search_fields=('specise_name',)  #  新增搜尋功能

class scientificAdmin(admin.ModelAdmin):
    list_display=('scientific_name', 'pub_date')   #  要顯示的欄位
    search_fields=('specise_name',)  #  新增搜尋功能


class data_typeAdmin(admin.ModelAdmin):
    list_display=['seq_format']   #  要顯示的欄位


class gene_infoAdmin(admin.ModelAdmin):
    list_display=('n_scientific', 'annotation', 'f_seq','date')    #  要顯示的欄位
    search_fields=('n_scientific','annotation') 


class reference_summaryAdmin(admin.ModelAdmin):
    list_display=('db_id', 'orgranism_name','top_type', 'Description','taxid')    #  要顯示的欄位
    search_fields=('db_id', 'orgranism_name', 'taxid') 


admin.site.register(models.Specise, SpeciseAdmin)
admin.site.register(models.scientific, scientificAdmin)
admin.site.register(models.data_type, data_typeAdmin)
admin.site.register(models.gene_info, gene_infoAdmin)
admin.site.register(models.reference_summary, reference_summaryAdmin)


