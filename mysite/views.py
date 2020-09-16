from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from mysite import models
from datetime import datetime
from django.contrib import auth
import pickle
from django.contrib.auth import views as auth_views
from mysite import views

## Login
def logout(request):
    auth.logout(request)
    return render(request,'./registration/logged_out.html/')

## View DB
def reference_summary(request):
    info = models.reference_summary.objects.all()
    
    total_count = 0
    bacteria_count = 0
    fungi_count = 0
    virus_count = 0
    archaea_count = 0
    parasite_count = 0
    Mycoplasma_count = 0
    
    for i in info:
        total_count = total_count + 1
        if i.top_type == "bacteria":
            bacteria_count += 1
        elif i.top_type == "archaea":
            archaea_count += 1
        elif i.top_type == "fungi":
            fungi_count += 1
        elif i.top_type == "virus":
            virus_count += 1
        elif i.top_type == "archaea":
            archaea_count += 1
        elif i.top_type == "parasite":
            parasite_count += 1
        elif i.top_type == "Mycoplasma/Chlamydia/Rickettsia":
            Mycoplasma_count += 1
# bacteria
# archaea
# fungi
# virus
# parasite
# Mycoplasma/Chlamydia/Rickettsia
                  
    
    now = datetime.now()
    return render(request, './content/call_db.html', locals())

def new_input(request):
    space_count=list(range(1,50))
    return render(request, './content/new_input.html', locals())


## input new data 
def new_input_check(request):
    def post_fuction(value):
        try:
            data = request.POST[value]
        except :
            data = ""
        return data
    
    def post_fuction_alarm(value):
        try:
            data = request.POST[value]
        except :
            data = ""
        
        if data == "":
            return render(request, './content/new_input.html', locals())
        else:
            return data
    
    
    if request.method == 'POST':
        now = datetime.now()
        s="S"
        db_id = post_fuction('db_id')
        organism_name =post_fuction('organism_name')
        chinese_name = post_fuction('chinese_name')
        genus = post_fuction('genus')
        top_type = post_fuction('top_type')
        species_name = post_fuction('species_name')
        
        ###### Key_words
        # Aerobic_ablity
        aerobic_ablity = post_fuction('Aerobic_ablity')
        ###### Pathogenic:
        pathogen = post_fuction('pathogen')
        opportunistic_pathogen = post_fuction('opportunistic_pathogen')
        plant_pathogen = post_fuction('plant_pathogen')
        unkown_pathogenic = post_fuction('unkown_pathogenic')
        keyword_pathogen=[ pathogen, opportunistic_pathogen, plant_pathogen, unkown_pathogenic]
        ### Flora/environmental:
        normal_flora = post_fuction('normal_flora')
        environmental = post_fuction('environmental')
        keyword_Flora= [normal_flora,environmental]
        ### Position:
        oral = post_fuction('oral')
        gut = post_fuction('gut')
        skin = post_fuction('skin')
        vaginal = post_fuction('vaginal')
        respiratory = post_fuction('respiratory')
        keyword_Position=[oral,gut,skin,vaginal,respiratory]
        ### Extrime type:
        extrime = post_fuction('extrime')
        acidophilic = post_fuction('acidophilic')
        thermophilic = post_fuction('thermophilic')
        halophilic = post_fuction('halophilic')
        keyword_Extrime = [extrime,acidophilic,thermophilic,halophilic]
        ### others :
        unkown = post_fuction('unkown')
        keyword_others = post_fuction('keyword_others')
        keyword_others_list=[unkown,keyword_others]
        #keyword=[aerobic_ablity,keyword_pathogen,keyword_Flora,keyword_Position,keyword_Extrime,keyword_others_list]
        keyword=[aerobic_ablity,pathogen,opportunistic_pathogen,plant_pathogen,unkown_pathogenic,normal_flora,environmental,oral,gut,skin,vaginal,respiratory,extrime,acidophilic,thermophilic,halophilic,unkown,keyword_others]
        #test=str(type(keyword))
        gram_stain = post_fuction('gram_stain')
        
        # sample_type
        blood = post_fuction('blood')
        plasma = post_fuction('plasma')
        CSF = post_fuction('CSF')
        BLAF = post_fuction('BLAF')
        sputum = post_fuction('sputum')
        pleural_fluid = post_fuction('pleural_fluid')
        ascites = post_fuction('ascites')
        positive_conpare = post_fuction('positive_conpare')
        negative_conpare = post_fuction('negative_conpare')
        tissue = post_fuction('tissue')
        sample_type=[blood,plasma,CSF,BLAF,sputum,pleural_fluid,ascites,positive_conpare,negative_conpare,tissue]

        Halos_id = post_fuction('Halos_id')
        taxid = post_fuction('taxid')
        species_taxid = post_fuction('species_taxid')
        the_user = post_fuction('source')
        Description = post_fuction('Description')
        reference1 = post_fuction('reference1')
        reference2 = post_fuction('reference2')
        reference3 = post_fuction('reference3')
        reference4 = post_fuction('reference4')
        reference5 = post_fuction('reference5')
        reference=[reference1,reference2,reference3,reference4,reference5]
        
        data_source = post_fuction('data_source')
        data_status = post_fuction('data_status')
        
        if organism_name == "" or genus == "" or top_type == "" or species_name == "" or Description == "" or reference1 == "" :
            message="error_blank"
            return render(request, './content/new_input.html', locals())
        message="Upload successfully"
        return render(request, './content/new_input_check.html', locals())
    else:
        return render(request, './content/new_input.html', locals())

def input_upload(request):
    def post_fuction(value):
        try:
            data = request.POST[value]
        except :
            data = ""
        return data
    if request.method == 'POST':
        
        # db_id,organism_name,chinese_name,genus,top_type,species_name,
        # keyword,gram_stain,sample_type,source,Description,Halos_id,
        # reference,data_source, data_status
        
        db_id=post_fuction('db_id')
        organism_name=post_fuction('organism_name')
        chinese_name = post_fuction('chinese_name')
        genus = post_fuction('genus')
        top_type = post_fuction('top_type')
        species_name = post_fuction('species_name')
        keyword = post_fuction('keyword')
        gram_stain = post_fuction('gram_stain')
        sample_type = post_fuction('sample_type')
        Halos_id = post_fuction('Halos_id')
        source = post_fuction('source')
        species_taxid = post_fuction('species_taxid')
        taxid = post_fuction('taxid')
        Description = post_fuction('Description')
        
        reference = post_fuction('reference')
        reference_list = reference.split(',')
        reference1 = reference_list[0]
        reference2 = reference_list[1]
        reference3 = reference_list[2]
        reference4 = reference_list[3]
        reference5 = reference_list[4]
        
        now = datetime.now()
        data_source = post_fuction('data_source')
        data_status = post_fuction('data_status')
        
        ## database upload (per single data)
        try:        
            obj = models.reference_summary.objects.get(db_id=db_id)
        except models.reference_summary.DoesNotExist:
            obj = models.reference_summary(db_id=db_id,organism_name=organism_name,chinese_name=chinese_name,genus=genus,species_name=species_name,gram_stain=gram_stain,top_type=top_type,source=source,key_word=keyword,sample_type=sample_type,Halos_id=Halos_id,taxid=taxid,species_taxid=species_taxid,Description=Description,reference1=reference1,reference2=reference2,reference3=reference3,reference4=reference4,reference5=reference5,date=now,data_source=data_source,data_status=data_status)
            obj.save()
            message="Upload_successfully"
        # db_id=db_id,organism_name=organism_name,chinese_name=chinese_name,genus=genus,species_name=species_name,gram_stain=gram_stain,top_type=top_type,source=source,key_word=key_word,sample_type=sample_type,Halos_id=Halos_id,taxid=taxid,species_taxid=species_taxid,Description=Description,reference1=reference1,reference2=reference2,reference3=reference3,reference4=reference4,reference5=reference5,date=now,data_source=data_source,data_status=data_status

        # POST value:
        # db_id,organism_name,chinese_name,
        # genus,top_type,species_name,
        # keyword,gram_stain,sample_type,
        # Halos_id,species_taxid,taxid,source,Description,
        # reference1,reference2,reference3,reference4,reference5,
        # now,data_source,data_status
        #
        # DB column:
        # db_id,organism_name,chinese_name,
        # genus,species_name,gram_stain,
        # top_type,source,key_word,sample_type,
        # Halos_id,taxid,species_taxid,Description,
        # reference1,reference2,reference3,reference4,reference5,
        # date,data_source,data_status
        
        return render(request, './content/new_input.html', locals())
    else:
        return render(request, './content/new_input.html', locals())

### Search db 
def search_result(request):
    if request.method == 'POST':
        now = datetime.now()
        category = request.POST['category']
        input_text = request.POST['input']
        
        try:
            the_user = request.POST['source']
        except KeyError:
            the_user = ""
        
        ##########################################
        ### Saving search log upload database 
        ### (input_word,category,date_time)
        try:        
            obj = models.db_search_log.objects.get( input_word=input_text, category=category,user=the_user,date_time=now)
        except models.db_search_log.DoesNotExist:
            obj = models.db_search_log( input_word=input_text,category=category,user=the_user,date_time=now)
            obj.save()
        
        if input_text in (''):
            return render(request, './content/search_result.html', locals())
        elif category in ('db_id'):
            entry_list = list(models.reference_summary.objects.filter(db_id__contains=input_text))
        elif category in ('organism_name'):
            entry_list = list(models.reference_summary.objects.filter(organism_name__contains=input_text))
            category="物種名"
        elif category in ('chinese_name'):
            entry_list = list(models.reference_summary.objects.filter(chinese_name__contains=input_text))
            category="中文名"
        elif category in ('genus'):
            entry_list = list(models.reference_summary.objects.filter(genus__contains=input_text))
            category="屬名"
        elif category in ('top_type'):
            entry_list = list(models.reference_summary.objects.filter(top_type__contains=input_text))
            category="大分類"
        elif category in ('source'):
            entry_list = list(models.reference_summary.objects.filter(source__contains=input_text))
            category="資料來源"
        elif category in ('Halos_id'):
            entry_list = list(models.reference_summary.objects.filter(Halos_id__contains=input_text))
        elif category in ('taxid'):
            entry_list = list(models.reference_summary.objects.filter(taxid__contains=input_text))
        elif category in ('key_word'):
            entry_list = list(models.reference_summary.objects.filter(key_word__contains=input_text))
        elif category in ('Description'):
            entry_list = list(models.reference_summary.objects.filter(Description__contains=input_text))
        
        total_count = 0
        bacteria_count = 0
        fungi_count = 0
        virus_count = 0
        archaea_count = 0
        parasite_count = 0
        Mycoplasma_count = 0
        
        for i in entry_list:
            total_count = total_count + 1
            if i.top_type == "bacteria":
                bacteria_count += 1
            elif i.top_type == "archaea":
                archaea_count += 1
            elif i.top_type == "fungi":
                fungi_count += 1
            elif i.top_type == "virus":
                virus_count += 1
            elif i.top_type == "archaea":
                archaea_count += 1
            elif i.top_type == "parasite":
                parasite_count += 1
            elif i.top_type == "Mycoplasma/Chlamydia/Rickettsia":
                Mycoplasma_count += 1
        return render(request, './content/search_result.html', locals())
        '''
        db = models.reference_summary.objects.extra(select={'category': 'SELECT * FROM reference_summary WHERE blog_entry.blog_id = blog_blog.id'})
        
        Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
        SELECT * FROM blog_entry WHERE (foo='a' OR bar='a') AND (baz='a')
        
        Blog.objects.get(name__iexact='beatles blog')
        SELECT ... WHERE name ILIKE 'beatles blog';
                
        Entry.objects.get(headline__contains='Lennon')
        SELECT ... WHERE headline LIKE '%Lennon%';
        
        inner_qs = Blog.objects.filter(name__contains='Cheddar')
        entries = Entry.objects.filter(blog__in=inner_qs)
        SELECT ... WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%')
        
        inner_qs = reference_summary.objects.filter(category.__contains=input_text)
        entries = Entry.objects.filter(reference_summary__in=inner_qs)
        SELECT * FROM reference_summary WHERE `$category` LIKE '%$input%' ORDER BY `$category` ASC
                
        extra(select={'is_recent': "pub_date > '2006-01-01'"})
        Blog.objects.extra(
            select={
                'entry_count': 'SELECT COUNT(*) FROM blog_entry WHERE blog_entry.blog_id = blog_blog.id'
            },
        )
        "SELECT * FROM reference_summary WHERE `$category` LIKE '%$input%' ORDER BY `$category` ASC"
        '''
    else:
        return render(request, './content/search_engine.html')




