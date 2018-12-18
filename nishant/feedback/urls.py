from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='feedback'),
    path('',views.Subscription,name='sub'),
    path('',views.Contact,name='contact'),

]