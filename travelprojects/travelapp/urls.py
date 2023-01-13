from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('sub/', views.subst, name='subst'),
    # path('mul/', views.mult, name='mult'),
    # path('div/', views.divi, name='divi'),

]
