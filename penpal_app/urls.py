from django.urls import path
from . import views 

urlpatterns = [
  path('',views.index,name='index'),
  path('notfound',views.notfound,name='notfound'),
  path('contact/',views.contact,name='contact'),
  path('editprofile/',views.editprofile,name='editprofile'),
  path('chat/',views.chat,name='chat'),
  path('faq/',views.faq,name='faq'),
  path('profile/',views.profile,name='profile'),
  path('tags',views.tags,name='tags'),
  path('chatbox',views.chatbox,name='chatbox'),
]