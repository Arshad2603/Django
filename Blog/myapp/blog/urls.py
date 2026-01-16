from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index" ),
    path("post/<slug:slug>", views.detail, name="detail"),
    path("puthu_puthu_url", views.puthu_url_paaru, name="puthu_url" ),
    path("pazhaiya_url", views.pazhaiya_url_redirect, name="pazhaiya_url" ),

]