
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.home),
    path('s',views.sub),
    path('s1',views.cal),
    path('s2',views.newcal),
    path('s3',views.list),
]
