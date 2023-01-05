from django.conf.urls.static import static
from django.urls import path

from news import settings
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', categories, name='cats')
]

handler404 = pageNotFound

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)