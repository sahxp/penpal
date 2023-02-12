from django.urls import path
from . import views 

urlpatterns = [
  path('',views.index,name='index'),
  path('',views.notfound,name='notfound'),
  path('',views.contact,name='contact'),
  path('',views.editprofile,name='editprofile'),
  path('',views.explore,name='explore'),
  path('',views.faq,name='faq'),
  path('profile/',views.profile,name='Profile'),
  path('',views.tags,name='tags'),
]