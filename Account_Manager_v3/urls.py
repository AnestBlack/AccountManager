"""Account_Manager_v3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from v3 import views as v3_views

urlpatterns = [
    path('',v3_views.index,name='home'),
    path('index/zh',v3_views.index_zh,name='index_zh'),
    path('search/',v3_views.search,name='search'),
    path('search/zh',v3_views.search_zh,name='search_zh'),
    path('Update/',v3_views.Update,name='Update'),
    path('Update/zh',v3_views.Update_zh,name='Update_zh'),
    path('Del/<str:keywordStr>',v3_views.Delete_Item,name='Delete_Item'),
    path('getAccount/<str:AddressStr>',v3_views.getAccount,name='getAccount'),
    path('getPassword_1/<str:AddressStr>/<str:AccountStr>',v3_views.getPassword_1,name='getPassword_1'),
    path('getPassword_2/<str:AddressStr>/<str:AccountStr>',v3_views.getPassword_2,name='getPassword_2'),
    path('getPassword_3/<str:AddressStr>/<str:AccountStr>',v3_views.getPassword_3,name='getPassword_3'),
    path('getPassword_max/<str:Password_3>',v3_views.getPassword_max,name='getPassword_max'),
    path('Save_Result/<str:AddressStr>/<str:AccountStr>/<str:password>/<str:Text>',v3_views.Save_Result_to_sql,name='Save_Result_to_sql'),
    path('searched/<int:keyInt>/<str:keywordStr>',v3_views.Search_Item,name='Search_Item'),
    path('Backup',v3_views.Backup_Database,name="backup"),
    path('Update_Text/<str:DateStr>/<str:TextStr>',v3_views.Update_Text,name='Update_text')
    #path('admin/', admin.site.urls),
    #path('Restore',v3_views.Restore_Database,name='restore'),
]
