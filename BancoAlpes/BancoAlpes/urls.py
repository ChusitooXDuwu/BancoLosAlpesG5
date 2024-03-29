"""BancoAlpes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

# from the folder documents, import the views file
from documents.views import pdf_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('cliente/', include('cliente.urls')),
    path('documents/', include('documents.urls')),
    

    #path('document/', pdf_view, name='pdf_view'),    
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^docsClientes/(?P<path>.*)$', serve, {
            'document_root': settings.DOC_ROOT,
        }),
        path('health-check/', views.healthCheck),
    ]