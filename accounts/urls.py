from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static
import django.contrib.auth.urls


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('myaccount/', views.profile, name='myaccount'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)