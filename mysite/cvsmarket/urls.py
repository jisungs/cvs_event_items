from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index' ),
    path('csvreader/', views.csv_reader, name='csv_reader' ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)