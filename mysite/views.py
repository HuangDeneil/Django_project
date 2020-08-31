from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite import models
from datetime import datetime
from django.contrib import auth


def index(request):
    now = datetime.now()
    return render(request, './content/homepage.html', locals())

def reference_summary(request):
    info = models.reference_summary.objects.all()
    now = datetime.now()
    return render(request, './content/call_db.html', locals())

def new_input(request):
    now = datetime.now()
    return render(request, './content/new_input.html', locals())

def search_engine(request):
    now = datetime.now()
    return render(request, './content/search_engine.html', locals())

def manage(request):
    info = models.reference_summary.objects.all()
    now = datetime.now()
    return render(request, './content/manage.html', locals())


def logout(request):
    auth.logout(request)
    return render(request,'./registration/logged_out.html/')

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


def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('blog_login')

    return render(request, 'blog/admin_page.html')
'''


# def detail(request, id):
#     try:
#         info = models.gene_info.objects.get(id=id)
#     except:
#         pass
#     return render(request, 'detail.html', locals())



