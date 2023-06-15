"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from notesapp.views import (

    home_screen_view,sign_up,sign_up_view,welcome_view,sign_in,create_note,view_my_notes,delete_note,view_all_notes,delete_notes,

    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home_screen_view,name='home_screen_view'),
    path("sign_up/",sign_up,name='sign_up'),
    path("sign_up_view",sign_up_view,name='sign_up_view'),
    path("welcome_view/",welcome_view,name='welcome_view'),
    path("sign_in/",sign_in,name='sign_in'),
    path("create_note/",create_note,name='create_note'),
    path("view_my_notes/",view_my_notes,name='view_my_notes'),
    path("delete_note/<int:note>/",delete_note,name='delete_note'),
    path("delete_notes/<int:note>/",delete_notes,name='delete_notes'),
    path("view_all_notes/",view_all_notes,name='view_all_notes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)