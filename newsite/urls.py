
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('result', views.resultview),
    path('res',views.resultviews),
    path('es',views.resultclass2),
]
