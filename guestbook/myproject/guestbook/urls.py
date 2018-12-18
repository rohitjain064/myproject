from django.urls import path,include
from.views import index,sign

urlpatterns = [
    path('',index,name='index'),
    path('sign/',sign,name='sign')
    ]