#cretae url to docuemtnos so i can lok fot them in the djangoa dmin

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.documents_view, name='documents_view'),
    path('<int:pk>', views.document_view, name='documento_view'),
]