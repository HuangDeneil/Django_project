from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite import models
from datetime import datetime
from django.contrib import auth

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

## Search db 
def search_result(request):
    now = datetime.now()
    return render(request, './content/search_result.html', locals())


## data
def data_detail(request):
    try:
        p = reference_summary.objects.get(db_id=db_id)
    except reference_summary.DoesNotExist:
        raise Http404('Cannot found objects')
    return render(request, 'disp.html', locals())


from django.shortcuts import render
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

'''
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

'''


# def detail(request, id):
#     try:
#         info = models.gene_info.objects.get(id=id)
#     except:
#         pass
#     return render(request, 'detail.html', locals())



