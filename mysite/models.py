from django.db import models
from django.utils import timezone

# Create your models here. 
class Specise(models.Model):  
    specise_name = models.CharField(max_length=20)
    note = models.TextField(default='備註')
    pub_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-pub_date',)
    
    def __str__(self):
        return self.specise_name

class scientific(models.Model):  
    scientific_name = models.CharField(max_length=40)
    note = models.TextField(default='備註')
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.scientific_name


class data_type(models.Model):  
    seq_format = models.CharField(max_length=8)

    def __str__(self):
        return self.seq_format

class gene_info(models.Model):   
    n_specise = models.ForeignKey('Specise', on_delete=models.CASCADE, verbose_name='物種')
    n_scientific = models.ForeignKey('scientific', on_delete=models.CASCADE, verbose_name='學名') # 當參照物件(ForeignKey)被刪除，此參照物件也會被刪除喔~  
    f_seq = models.ForeignKey('data_type', on_delete=models.CASCADE, verbose_name='序列格式')
    sequence = models.TextField(default='example\n>seq \nATCGATGC')
    annotation = models.CharField(max_length=50)
    description = models.TextField(default='暫無說明')  
    date = models.DateField(auto_now=True)
    
    class Meta:
      #  ordering = ('pub_date',)   #  正排序
        ordering = ('-date',) #  反排序

    def __str__(self):
        return self.annotation


class reference_summary(models.Model): 
    db_id = models.CharField(max_length=30, blank=True, null=True)
    orgranism_name = models.CharField(max_length=100, blank=True, null=True, default='')  # 當參照物件(ForeignKey)被刪除，此參照物件也會被刪除喔~  
    chinese_name = models.CharField(max_length=100, null=True, blank=True, default='')  
    genus = models.CharField(max_length=100, null=True, blank=True, default='')  
    species_name = models.CharField(max_length=100, blank=True, null=True, default='')  
    gram_stain = models.CharField(max_length=100, blank=True,null=True, default='')  
    top_type = models.CharField(max_length=100, blank=True,null=True, default='') 
    source = models.CharField(max_length=200, blank=True,null=True, default='')  ## input user name
    key_word = models.TextField(blank=True, null=True, default='')  
    Halos_id = models.CharField(max_length=100, null=True, blank=True, default='')  
    taxid = models.CharField(max_length=100, blank=True, null=True, default='')  
    Description = models.TextField(null=True, blank=True, default='')  
    reference1 = models.TextField(null=True, blank=True)  
    reference2 = models.TextField(null=True, blank=True)  
    reference3 = models.TextField(null=True, blank=True)  
    reference4 = models.TextField(null=True, blank=True)  
    reference5 = models.TextField(null=True, blank=True)  
    date = models.DateField(null=True, blank=True, auto_now=True)
    data_source = models.CharField(max_length=200,null=True, default='unknow', blank=True)  
    data_status = models.CharField(max_length=200,null=True, default='unknow', blank=True)  

    class Meta:
      #  ordering = ('pub_date',)   #  正排序
        ordering = ('-date',) #  反排序

    def __str__(self):
        return self.orgranism_name


