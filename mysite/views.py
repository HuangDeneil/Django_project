from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    now = datetime.now()
    return render(request, './content/call_db.html', locals())

## check POST value is not Null 
def post_fuction(value):
    #print(value)
    
    try:
        data = request.POST['source']
    except :
        data = "unknown"
        
    return data
    #return str('request.POST[\''+value+'\']')


## input new data 
def new_input(request):
    now = datetime.now()
    
    db_id= request.POST['db_id']
    try:
        db_id = request.POST['db_id']
    except KeyError:
        db_id = ""
    if db_id == "":
        dbid = now | "Y M d h:i:s"
    
    organism_name = request.POST['organism_name']
    chinese_name = request.POST['chinese_name']
    genus = request.POST['genus']
    top_type = request.POST['top_type']
    species_name = request.POST['species_name']
    
    ###### Key_words
    # Aerobic_ablity
    try:
        aerobic_ablity = request.POST['Aerobic_ablity']
    except KeyError:
        aerobic_ablity = "unknown_aerobic_ablity"
    
    ###### Pathogenic:
    # pathogen
    try:
        pathogen = request.POST['pathogen']
    except KeyError:
        pathogen = ""
    # opportunistic_pathogen
    try:
        opportunistic_pathogen = request.POST['opportunistic_pathogen']
    except KeyError:
        opportunistic_pathogen = ""
    # plant_pathogen
    try:
        plant_pathogen = request.POST['plant_pathogen']
    except KeyError:
        plant_pathogen = ""
    # unkown_pathogenic
    try:
        unkown_pathogenic = request.POST['unkown_pathogenic']
    except KeyError:
        unkown_pathogenic = ""
    keyword_pathogen=[ pathogen, opportunistic_pathogen, plant_pathogen, unkown_pathogenic]
    
    ### Flora/environmental:
    # normal_flora
    try:
        normal_flora = request.POST['normal_flora']
    except KeyError:
        normal_flora = ""
    # environmental
    try:
        environmental = request.POST['environmental']
    except KeyError:
        environmental = ""
    keyword_Flora= [normal_flora,environmental]
    
    ### Position:
    # oral
    try:
        oral = request.POST['oral']
    except KeyError:
        oral = ""
    # gut
    try:
        gut = request.POST['gut']
    except KeyError:
        gut = ""
    # skin
    try:
        skin = request.POST['skin']
    except KeyError:
        skin = ""
    # vaginal
    try:
        vaginal = request.POST['vaginal']
    except KeyError:
        vaginal = ""
    # respiratory
    try:
        respiratory = request.POST['respiratory']
    except KeyError:
        respiratory = ""
    keyword_Position=[oral,gut,skin,vaginal,respiratory]
    
    ### Extrime type:
    # extrime
    try:
        extrime = request.POST['extrime']
    except KeyError:
        extrime = ""
    # acidophilic
    try:
        acidophilic = request.POST['acidophilic']
    except KeyError:
        acidophilic = ""
    # thermophilic
    try:
        thermophilic = request.POST['thermophilic']
    except KeyError:
        thermophilic = ""
    # halophilic
    try:
        halophilic = request.POST['halophilic']
    except KeyError:
        halophilic = ""
    keyword_Extrime = [extrime,acidophilic,thermophilic,halophilic]
    ### others :
    # unkown
    try:
        unkown = request.POST['unkown']
    except KeyError:
        unkown = ""
    
    # keyword_others
    try:
        keyword_others = request.POST['keyword_others']
    except KeyError:
        keyword_others = ""
    keyword_others_list=[unkown,keyword_others]
    
    #gram_stain
    try:
        gram_stain = request.POST['gram_stain']
    except KeyError:
        gram_stain = ""
    
    # sample_type
    #blood
    # plasma
    # CSF
    # BLAF
    # sputum
    # pleural_fluid
    # ascites
    # positive_conpare
    # negative_conpare
    # tissue
    # sample_type_others
    
    
    # Halos_id
    try:
        Halos_id = request.POST['Halos_id']
    except KeyError:
        Halos_id = ""
    # taxid
    try:
        taxid = request.POST['taxid']
    except KeyError:
        taxid = ""
    #species_taxid
    try:
        species_taxid = request.POST['species_taxid']
    except KeyError:
        species_taxid = ""
    
    try:
        the_user = request.POST['source']
    except KeyError:
        the_user = "unknown"
    
    
    
    
    # Description
    try:
        Description = request.POST['Description']
    except KeyError:
        Description = ""
    # reference1
    try:
        reference1 = request.POST['reference1']
    except KeyError:
        reference1 = ""
    # reference2
    try:
        reference2 = request.POST['reference2']
    except KeyError:
        reference2 = ""
    # reference3
    try:
        reference3 = request.POST['reference3']
    except KeyError:
        reference3 = ""
    # reference4
    try:
        reference4 = request.POST['reference4']
    except KeyError:
        reference4 = ""
    # reference5
    try:
        reference5 = request.POST['reference5']
    except KeyError:
        reference5 = ""
    # data_source
    try:
        data_source = request.POST['data_source']
    except KeyError:
        data_source = ""
    # data_status
    try:
        data_status = request.POST['data_status']
    except KeyError:
        data_status = ""
    
    return render(request, './content/new_input_check.html', locals())

### Search db 
def search_result(request):
    if request.method == 'POST':
        now = datetime.now()
        category = request.POST['category']
        input_text = request.POST['input']
        
        try:
            the_user = request.POST['source']
        except KeyError:
            the_user = "unknown"
        try:        
            obj = models.db_search_log.objects.get( input_word=input_text, category=category,user=the_user,date_time=now)
        except models.db_search_log.DoesNotExist:
            obj = models.db_search_log( input_word=input_text,category=category,user=the_user,date_time=now)
            obj.save()
        
        if input_text in (''):
            return render(request, './content/search_result.html', locals())
        elif category in ('db_id'):
            entry_list = list(models.reference_summary.objects.filter(db_id__contains=input_text))
        elif category in ('orgranism_name'):
            entry_list = list(models.reference_summary.objects.filter(orgranism_name__contains=input_text))
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
        
        ## saving search log
        #(input_word,category,date_time)
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






'''
## data
def data_detail(request):
    try:
        p = reference_summary.objects.get(db_id=db_id)
    except reference_summary.DoesNotExist:
        raise Http404('Cannot found objects')
    return render(request, 'disp.html', locals())

def comment(request, id):
    if id:
        r = Restaurant.objects.get(id=id)
    else:
        return HttpResponseRedirect("restaurants_list")
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now()) # 擷取現在時間
        Comment.objects.create(visitor=visitor, email=email, content=content, date_time=date_time, restaurant=r)
    return render(request, 'comments.html', locals())

def list_restaurants(request):
    restaurants = models.Restaurant.objects.all()
    return render_to_response('./restaurants_list.html', locals())

def login(request):
    if request.user.is_authenticated():
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'blog/login.html')
def detail(request, id):
    try:
        info = models.gene_info.objects.get(id=id)
    except:
        pass
    return render(request, 'detail.html', locals())
'''