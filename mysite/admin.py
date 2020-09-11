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
    list_display=('db_id', 'orgranism_name','top_type', 'key_word', 'Description','taxid')    #  要顯示的欄位
    search_fields=('db_id', 'orgranism_name', 'taxid') 


class db_search_logAdmin(admin.ModelAdmin):
    list_display=('user','input_word','category','date_time') 
    search_fields=('user','input_word','category','date_time') 

'''
class CommentAdmin(admin.ModelAdmin):
    list_display=('content', 'visitor','email', 'date_time')    #  要顯示的欄位
    search_fields=('content', 'visitor','email', 'date_time') 


class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name', 'phone_number','address')    #  要顯示的欄位
    search_fields=('name', 'phone_number','address')  
'''
admin.site.register(models.Specise, SpeciseAdmin)
admin.site.register(models.scientific, scientificAdmin)
admin.site.register(models.data_type, data_typeAdmin)
admin.site.register(models.gene_info, gene_infoAdmin)
admin.site.register(models.reference_summary, reference_summaryAdmin)
admin.site.register(models.db_search_log, db_search_logAdmin)

#admin.site.register(models.Comment, CommentAdmin)
#admin.site.register(models.Restaurant, RestaurantAdmin)

