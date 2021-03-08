from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from mysite import models
from datetime import datetime
from django.contrib import auth
from django.contrib.auth import views as auth_views
from mysite import views
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


####################
###              ###
###  Login page  ###
###              ###
####################
def logout(request):
    auth.logout(request)
    return render(request,'./registration/logged_out.html/')



##################
###            ###
###   View DB  ###
###            ###
##################
def reference_summary(request):
    info = models.reference_summary.objects.order_by('db_id')
    #sorted(info, key=lambda car: car.compute_score)
    
    
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



########################
###                  ###
###  Input new data  ###
###     (填新表單)    ###
###                  ###
########################
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


#########################
###                   ###
###  Upload new data  ###
###   (上傳新表單)     ###
###                   ###
#########################
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

###########################
#####                 #####
#####    Search db    #####
#####                 #####
###########################
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
            category="db_id"
        elif category in ('organism_name'):
            entry_list = list(models.reference_summary.objects.filter(organism_name__contains=input_text))
            category="物種名"
        elif category in ('chinese_name'):
            entry_list = list(models.reference_summary.objects.filter(chinese_name__contains=input_text))
            category="中文名"
        elif category in ('genus'):
            entry_list = list(models.reference_summary.objects.filter(genus__contains=input_text))
            category="屬名"
        elif category in ('gram_stain'):
            entry_list = list(models.reference_summary.objects.filter(gram_stain__contains=input_text))
            category="gram_stain"
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




################################
#####                      #####
#####      Statistics      #####
#####  建立統計資訊現場畫圖  #####
#####                      #####
################################
def statistics(request):
    info = models.reference_summary.objects.order_by('db_id')
    
    total_count = 0
    bacteria_count = 0
    fungi_count = 0
    virus_count = 0
    archaea_count = 0
    parasite_count = 0
    Mycoplasma_count = 0

    tmp=""
    tmp_list=[]
    
    microorganism_name_list = []
    halos_id_count = 0
    key_word_count = 0
    microorganism_name={}
    halos_id_dict={}
    key_word_dict={}
    
    for i in info:
        total_count += 1
        if i.top_type == "bacteria":
            bacteria_count += 1
        elif i.top_type == "archaea":
            archaea_count += 1
        elif i.top_type == "fungi":
            fungi_count += 1
        elif i.top_type == "virus":
            virus_count += 1
        elif i.top_type == "parasite":
            parasite_count += 1
        elif i.top_type == "Mycoplasma/Chlamydia/Rickettsia":
            Mycoplasma_count += 1
        
        if i.organism_name:
            microorganism_name_list.append(str(i.organism_name))
            #microorganism_name[(str(i.organism_name))] += 1
            tmp_list = str(i.Halos_id).split(', ')
            halos_id_count = (len(tmp_list)-1)
            halos_id_dict[str(i.organism_name)] = halos_id_count
            tmp_list = str(i.key_word).split(', ')
            key_word_count = (len(tmp_list))
            key_word_dict[str(i.organism_name)] = key_word_count

    data_dict={}
    data_dict["bacteria"]=(bacteria_count)
    data_dict["fungi"]=(fungi_count)
    data_dict["virus"]=(virus_count)
    data_dict["archaea"]=(archaea_count)
    data_dict["parasite"]=(parasite_count)
    data_dict["Mycoplasma/Chlamydia/Rickettsia"]=(Mycoplasma_count)    
    
    name1 = np.array(data_dict.keys())
    count2 =(data_dict.values())
    
    name=[]
    count=[]
    for i in data_dict.keys():
        name.append(i)   
        count.append(data_dict[i])
    
    # colors = {
    #     'bacteria':'#F08080', 
    #     'fungi':'#3cb44b', 
    #     'virus':'#F3E7B1',
    #     'archaea': '#868497',
    #     'parasite':"#f58231",
    #     'Mycoplasma.Chlamydia.Rickettsia':"#73C2FB"
    #     }
    colors = ['cornflowerblue','darkorange','forestgreen','crimson','mediumpurple','sienna']

    
    #############################
    #####                  ######
    #####   pie plot 圖示  ######
    #####                  ######
    #############################
    fig1, ax1 = plt.subplots()
    wedges, texts, autotexts = ax1.pie(
        count,
        #labels=name,
        colors=colors,
        autopct='',
        pctdistance = 1.2,
        startangle=0,
        rotatelabels = 270,
        shadow = False,
        counterclock = False,
        radius=0
        )
    ax1.legend(wedges, name,
            title="Types ",
            loc="center left",
            bbox_to_anchor=(-0.05, 0.1))
    plt.setp(autotexts, size=10, weight="bold")
    plt.savefig("./static/images/legend.png" )   # save the figure to file 
    plt.close()
    
    ########################
    #####             ######
    #####   pie plot  ######
    #####             ######
    ########################
    fig1, ax1 = plt.subplots()
    wedges, texts, autotexts = ax1.pie(
        count,
        #labels=name,
        colors=colors,
        autopct='%1.1f%%',
        pctdistance = 1.2,
        startangle=0,
        rotatelabels = 270,
        shadow = False,
        counterclock = False,
        radius=1
        )
    ax1.axis("off")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.setp(autotexts, size=9, weight="bold")
    ax1.set_title("Composition of database")
    plt.savefig("./static/images/Pie_plot.png", dpi=400 )   # save the figure to file 
    plt.close()
    
    
    #############################################
    #####                                  ######
    #####  Microorganism_report_frequency  ######
    #####                                  ######
    #############################################
    name = []
    name = np.array( microorganism_name_list )
    x = list( range( len(name) ) )
    y = []
    
    for i in halos_id_dict.keys():
        y.append(halos_id_dict[i])
    txt = np.array( microorganism_name_list )
    plt.figure(figsize = (20,10))
    plt.scatter(x, y)
    
    taq=""
    for i in range(len(x)):
        taq = ("("+txt[i]+","+str(y[i])+")")
        if y[i] >22:
            plt.annotate( taq, xy = (i, y[i]), xytext = (i+0.1, y[i]+0.5) , fontsize=16)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)   
    plt.xlabel('Microorganism index', fontsize=20)
    plt.ylabel('Reported counts', fontsize=20) 
    plt.title('Microorganism report frequency', fontsize=28, color='black')
    
    plt.savefig("./static/images/Microorganism_report_frequency.png" , dpi=400)   # save the figure to file
    plt.close()
    
    halos_id_dict ={}
    data_dict ={}
    txt =[]
    #############################################
    #####                                  ######
    #####   Microorganism_keyword_count    ######
    #####                                  ######
    #############################################
    name = []
    name = np.array( microorganism_name_list )
    x = list( range( len(name) ) )
    y = []
    x = len(x)
    name = []
    for i in key_word_dict.keys():
        #name.append(i)   
        y.append(key_word_dict[i])
    txt = np.array( microorganism_name_list )
    
    key_word_dict ={}
    
    
    length_dict = {}
    tmp=0
    for i in range(len(y)):
        tmp = int( y[i] )
        #length_dict[tmp] = "test"
        try:
            length_dict[tmp] += 1 
        except KeyError:
            length_dict[tmp] = 0
    
    
    len_name = []
    len_disbuted = []
    
    len_name = np.array(list(sorted(length_dict.keys())))
    len_disbuted = list(range(len(len_name)))
    
    for i in list(range(len(len_name))):
        len_disbuted[i] = int(length_dict[len_name[i]])
    
    
    x=len_name
    y=len_disbuted
    txt =x
    bar_width = 0.5
    
    
    plt.figure(figsize = (20,10))
    plt.bar(len_name,
            len_disbuted,
            bar_width,      # 設定長條寬度
            alpha=.6
            )
    
    
    taq=""
    k=1
    for i in range(len(len_disbuted)):
        taq = (str(y[i]))
        plt.annotate( taq, xy = ((i+1), y[i]), xytext = (i+0.85, y[i]+3) , fontsize=16)
        #print("<p>"+i+","+y[i]+"</p>")
    plt.xticks(len_name,fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('keyword counts', fontsize=20)
    plt.ylabel('Microorganism counts', fontsize=20) 
    # #plt.title('Microorganism report frequency', fontsize=28, color='black')
    
    plt.savefig("./static/images/Microorganism_keyword_count.png" , dpi=400)   # save the figure to file
    plt.close()
    
    
    return render(request, './content/statistics.html', locals())


def my_view(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', locals())



def file_upload(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'file_upload_test.html', locals())
