from django.urls import path
from May import views

urlpatterns=[
    path('indexpage/',views.indexpage,name='indexpage'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('savecat',views.savecat,name='savecat'),
    path('displaycategory/', views.displaycategory, name='displaycategory'),
    path('editcategory/<int:dataid>/', views.editcategory, name='editcategory'),
    path('updatecat/<int:dataid>/', views.updatecat, name='updatecat'),
    path('deletecategory/<int:dataid>/', views.deletecategory, name='deletecategory'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('savepro/', views.savepro, name='savepro'),
    path('displayproduct/', views.displayproduct, name='displayproduct'),
    path('displaycontact/', views.displaycontact, name='displaycontact'),
    path('editpro/<int:dataid>/', views.editpro, name='editpro'),
    path('updatepro/<int:dataid>/', views.updatepro, name='updatepro'),
    path('deletepro/<int:dataid>/', views.deletepro, name='deletepro'),
    path('', views.adminlogin, name='adminlogin'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
]