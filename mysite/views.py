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



