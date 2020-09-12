from . import views

from django.urls import path
urlpatterns=[ 
path('showregistration/',views.showregistration,name='showregistration'),   
path('showregistration/registration/',views.registration,name='registration'),
path('show/',views.show,name='show'),
path('show/login/',views.login,name='login'),
path('logout/',views.logout,name='logout'),
]