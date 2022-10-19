from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('products/<pk>', views.product_details,name='product'),
    path('products/', views.product_list,name='productList'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)