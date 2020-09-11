from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite import models
from datetime import datetime
from django.contrib import auth
import pickle
from django.contrib.auth import views as auth_views

## Login
def logout(request):
    auth.logout(request)
    return render(request,'./registration/logged_out.html/')

## View DB
def reference_summary(request):
    info = models.reference_summary.objects.all()
    now = datetime.now()
    return render(request, './content/call_db.html', locals())

## input new data 
def new_input(request):
    now = datetime.now()
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