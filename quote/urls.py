from django.urls import path
from . import views


app_name = 'quote'
urlpatterns = [

    path('', views.home, name='home'),
    path('offer', views.offer, name='offer'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('faq', views.faq, name='faq'),
    ]
