from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from uploadfile import models
# from mysite import models
from datetime import datetime



import pickle
import re
import os
import sys
import numpy as np
import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import time
import subprocess

## upload model
from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from django.core.files.storage import default_storage






# Create your views here.

###################################
#####                         #####
#####   primary upload page   #####
#####                         #####
###################################
def file_upload(request):
    # print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload your file!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            
            input_text = request.POST['input']
            
            ########################################################
            #####                                              #####
            #####   Redirect to the document list after POST   #####
            #####                                              #####
            ########################################################
            return redirect('file-upload')                 

        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, './content/file_upload_test.html', locals())





###################################
#####                         #####
#####   primary upload page   #####
#####                         #####
###################################
def read_upload(request):
    if request.method == 'POST':
        now = datetime.now()
        # category = request.POST['category']
        input_text = request.POST['input']
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            
            # Redirect to the document list after POST
            #return redirect('read_file')
        else:
            message = 'The form is not valid. Fix the following error:'
        file_name = newdoc.docfile
        
        documents = models.Document.objects.filter(docfile__contains=file_name)
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        media_path = os.path.join(BASE_DIR, 'media')
        reads_file_name = (media_path+"/"+str(file_name))
        
        
        upload_file = pd.read_csv(reads_file_name)  

        # k = 0
        # data={}
        # with open(reads_file_name, mode = "r", encoding = "utf8") as file:
        #     for i in file:
        #         readline = i.rstrip()
                
        #         try :
        #             data[k] = str(readline)
        #         except KeyError:
        #             data[k] = str(readline)
        #         k+=1
        #         #
        # data_keys = data.keys()
        
        return render(request, './content/read_file.html', locals())

    else:
        return redirect('file-upload')
