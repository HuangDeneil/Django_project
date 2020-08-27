from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite import models
from datetime import datetime

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
    return render(request, './registration/logout.html', locals())

   

# def detail(request, id):
#     try:
#         info = models.gene_info.objects.get(id=id)
#     except:
#         pass
#     return render(request, 'detail.html', locals())



