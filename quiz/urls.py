from django.contrib import admin
from django.urls import path, include

from mainapp.views import index, catalogs

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('catalog/', catalogs, name='catalog'),
    path('accounts/', include('django.contrib.auth.urls')),
]
