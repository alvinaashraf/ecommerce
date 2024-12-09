
from xml.dom.expatbuilder import DOCUMENT_NODE

from django.contrib import admin
from django.urls import path
from . import views
#import for settings


urlpatterns = [
    path('',views.store,name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail')
]
