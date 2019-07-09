
from django.contrib import admin
from django.urls import path
from yuva import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('single/', views.single, name = 'Blog'),
    #path('contactform/',views.contactform,name='contactform'),
    path('emailSubscribe/', views.emailSubscribe, name='emailSubscribe'),
]