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


def new_input_check(request):
    db_id = request.POST['id']
    orgranism_name = request.POST['orgranism_name']
    chinese_name = request.POST['chinese_name']
    '''
    genus = request.POST['genus']
    top_type = request.POST['top_type']
    species_name = request.POST['species_name']
    ############################
    ###### key words start #####
    #Aerobic/anaerobic:
    aerobic_ablity = request.POST['Aerobic_ablity']
    #Pathogenic:
    pathogen = request.POST['pathogen']
    opportunistic_pathogen = request.POST['opportunistic_pathogen']
    plant_pathogen = request.POST['plant_pathogen']
    unkown_pathogenic = request.POST['unkown_pathogenic']
    #Flora/environmental:
    normal_flora = request.POST['normal_flora']
    environmental = request.POST['environmental']
    #Position:
    oral = request.POST['oral']
    gut = request.POST['gut']
    skin = request.POST['skin']
    vaginal = request.POST['vaginal']
    respiratory = request.POST['respiratory']
    #Extrime type:
    extrime = request.POST['extrime']
    acidophilic = request.POST['acidophilic']
    thermophilic = request.POST['thermophilic']
    halophilic = request.POST['halophilic']
    unkown = request.POST['unkown']
    others = request.POST['others']
    key_word_aerobic_ablity=[aerobic_ablity]
    key_word_pathogenic=[pathogen,opportunistic_pathogen,plant_pathogen,unkown_pathogenic]
    key_word_flora_environmental=[normal_flora,environmental]
    key_word_position = [oral, gut, skin, vaginal, respiratory]
    key_word_extrime_type = [extrime,acidophilic,thermophilic,halophilic]
    key_word_others = [others,unkown]
    ###### key words end #####
    ##########################
    gram_stain = request.POST['gram_stain']
    sample_type = request.POST['sample_type']
    source = request.POST['source']
    Halos_id = request.POST['Halos_id']
    taxid = request.POST['taxid']
    species_taxid = request.POST['species_taxid']
    source = request.POST['source']
    Description = request.POST['Description']
    reference1 = request.POST['reference1']
    reference2 = request.POST['reference2']
    reference3 = request.POST['reference3']
    reference4 = request.POST['reference4']
    reference5 = request.POST['reference5']
    data_source = request.POST['data_source']
    data_status = request.POST['data_status']
    '''
    date = timezone.localtime(timezone.now()) # 擷取現在時間
    #reference_summary.objects.create(db_id=db_id, orgranism_name=orgranism_name, chinese_name=chinese_name, genus=genus, gram_stain=gram_stain, top_type=top_type, source=source, key_word=key_word, Halos_id=Halos_id, taxid=taxid,Description=source,reference1=reference1, reference2=reference2, reference3=reference3, reference4=reference4, reference5=reference5,date=date,data_source=data_source,data_status=data_status )
    return render(request, './content/new_input_data_check.html', locals())


## Search db 
def search_result(request):
    now = datetime.now()
    category = request.POST['category']
    input_text = request.POST['input']
    return render(request, './content/search_result.html', locals())






'''
(db_id,orgranism_name,chinese_name, genus,species_name,
gram_stain, top_type, source, key_word, Halos_id, taxid,
Description,
reference1,reference2,reference3,reference4,reference5,
date,data_source,data_status)
'''


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



