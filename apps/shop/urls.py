from django.urls import path
from django.conf.urls import url
import apps.shop.views as views

urlpatterns = [
    # url(r'^$',views.index),
    # path('',views.index),
    path('login/', views.index, name='login'),
    path('check_user/', views.check_user, name='check_user'),
    path('register/', views.register),
    path('jump_register/', views.jump_register),
    path('jump_login', views.jump_login),
    path('register_to_db', views.register_to_db),
    path('Level1/', views.Level1),
    path('Level2/', views.Level2),
    path('CompareFlag', views.CompareFlag),
    path('Hide_Level2/', views.Hide_Level2),
    path('Level3/', views.Level3),
    path('Level4/', views.Level4),
    path('Level5/', views.Level5),
    path('Level6/', views.Level6),
    path('Level7/', views.Level7),
    path('Fake_end/', views.Fake_end),
    path('True_end/', views.True_end),
    path('LastGame/', views.LastGame),
    # path(r'^check_user/$', views.check_user, name='check_user'),

]
