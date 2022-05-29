from django.contrib import admin
from django.urls import path, include

from mainapp.views import index, catalogs, test, question, registration

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('catalog/<int:pk>/', catalogs, name='catalog'),
    path('catalog/', catalogs, name='catalog'),
    path('catalog/test/<int:pk>/', test, name='test'),
    path('catalog/test/<int:pk>/question/<int:page>/', question, name='question'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration, name='registration'),
]
