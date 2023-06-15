from django.urls import path
from WebApp import views

urlpatterns=[
    path('homepage/',views.homepage,name='homepage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('savecontact/', views.savecontact, name='savecontact'),
    path('catpro/<cat_name>/', views.catpro, name='catpro'),
    path('shopproduct/', views.shopproduct, name='shopproduct'),
    path('singlepro/<int:dataid>/', views.singlepro, name='singlepro'),
    path('ureg/', views.ureg, name='ureg'),
    path('saveuser/', views.saveuser, name='saveuser'),
    path('maylogin/', views.maylogin, name='maylogin'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('savecart/', views.savecart, name='savecart'),
    path('cart/',views.cart,name='cart'),
    path('deleteitem/<int:dataid>/', views.deleteitem, name='deleteitem'),
    path('checkout/', views.checkout, name='checkout'),
    path('orderplace/', views.orderplace, name='orderplace'),
]