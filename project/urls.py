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
    path('admin/', admin.site.urls),
    path('homepage', TemplateView.as_view(template_name='home.html')),
    path('home', TemplateView.as_view(template_name='home.html')),
    path('', TemplateView.as_view(template_name='home.html')),
    
    ## view db
    path('db', views.reference_summary),
    
    ## input new data for non-developer
    path('new_input', views.new_input),
    
    ## search engine non-developer
    path('search_engine', views.search_engine),
    
    ## login interface
    path('accounts/', include('django.contrib.auth.urls')),
    #path('logout', auth_views.PasswordChangeView.as_view() ),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='login_direction.html')),

    #path('', TemplateView.as_view(template_name='./content/homepage.html'))
    #path('login', views.login_action),
    #path('manage', admin.site.urls),
    #path('logout', views.logout),



    ### OAuth2 setting
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ### using re_path
    #re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #path('detail/<int:id>', views.detail, name = 'detail-url'),
]
