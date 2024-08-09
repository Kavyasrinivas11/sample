from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('login',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('viewall',views.viewall,name='viewall'),
    path('updatereg/<str:pk>/',views.updatereg,name='updatereg'),
    path('updatereg/updatedata/<str:pk>',views.updatedata,name='updaterecord'),
    path('deletereg/<str:pk>/',views.updatereg,name='deletereg')
]

