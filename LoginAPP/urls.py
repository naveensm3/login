from django.urls import path

from LoginAPP import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_fun,name='login'),
    path('register',views.register_fun,name='register'),
    path('read_register',views.read_register,name='read_register'),
    path('read_login',views.read_login,name='read_login'),
    path('logout',views.logout_fun,name='logout'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('readstudentdata', views.readstudentdata, name='readstudentdata'),
    path('studentdata/<int:id>',views.updatedata_fun,name='studentdata'),
    path('display',views.display_fun,name='display'),
    path('deletedata/<int:id>',views.deletedata_fun,name='deletedata'),

]