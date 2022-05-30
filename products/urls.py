from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list-items/',views.list_items,name='list_items'),
    path('email/',views.email, name='email'),
    path('phone/',views.phone, name='phone'),
    path('office-address/',views.office_address, name='office_address'),
    path('about-us/',views.about_us, name='about_us'),
]
