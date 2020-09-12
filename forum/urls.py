from . import views
from django.urls import path

urlpatterns=[ 
path('landing/',views.landing,name='landing'),
path('',views.forummain,name='forummain'), 
path('displaycomments/<int:id>', views.displaycomments),
path('postnew/',views.postnew,name='postnew'),
path('commentnew/<int:id>',views.commentnew,name='commentnew'),
path('forum/myposts/',views.myposts,name='myposts'),
path('forum/myposts/editpost/<int:id>',views.editpost,name='editpost'),
path('forum/myposts/deletepost/<int:id>',views.deletepost,name='deletepost'),
path('forum/mycomments/',views.mycomments,name='mycomments'),
path('forum/mycomments/editcomment/<int:id>',views.editcomment,name='editcomment'),
path('forum/mycomments/deletecomment/<int:id>',views.deletecomment,name='deletecomment'),
]