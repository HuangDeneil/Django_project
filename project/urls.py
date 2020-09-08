"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from mysite import views
from django.views.generic.base import TemplateView
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    # My django primary administry back-end
    path('admin/', admin.site.urls),
    
    # My root page
    path('homepage', TemplateView.as_view(template_name='./content/home.html')),
    path('home', TemplateView.as_view(template_name='./content/home.html')),
    path('Home', TemplateView.as_view(template_name='./content/home.html')),
    path('', TemplateView.as_view(template_name='./content/home.html')),
    
    ## view db
    path('db', views.reference_summary),
    
    ## input new data for non-developer
    path('new_input', views.new_input),
    
    ## search engine non-developer
    path('search_engine', TemplateView.as_view(template_name='./content/search_engine.html')),
    path('search_result', views.search_result),
    
    # manage 
    path('manage',TemplateView.as_view(template_name='./content/manage.html')),

    ## login interface
    path('accounts/', include('django.contrib.auth.urls')),


    path('restaurants_list', views.list_restaurants),
    path('restaurants_list/', views.list_restaurants),
    ### OAuth2 setting
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ### using re_path
    #re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #path('detail/<int:id>', views.detail, name = 'detail-url'),
]
