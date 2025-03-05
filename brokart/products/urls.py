
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("product_list",views.list_products,name='list_product')
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)