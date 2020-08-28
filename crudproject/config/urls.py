"""crudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from blog.views import new, index, create, detail, delete, edit, update, memoform, comment_create, comment_delete

import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('new/', new, name = 'new'),
    path('create/', create, name = 'create'),
    path('memo/<int:memo_id>/', detail, name = 'detail'),
    path('memo/delete/<int:memo_id>/', delete, name = 'delete'),
    path('memo/edit/<int:memo_id>/', edit, name = 'edit'),
    # path('memo/update/<int:memo_id>/', update, name = 'update'),        
    path('memo/update/<int:memo_id>/', update, name = 'update'),     
    path('memoform/', memoform, name = 'memoform'),
    # path('memo/<int:memo_id>/', commentcreate, name = 'commentcreate'),
    path('comment_create/<int:memo_id>',comment_create, name="comment_create" ),
    path('comment_delete/<int:post_id>/<int:com_id>', comment_delete, name="comment_delete"),
    path('accounts/', include('accounts.urls')),

    path('accountss/', include('allauth.urls'))
] 

