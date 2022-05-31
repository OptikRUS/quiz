from django.contrib import admin
from django.urls import path, include

from mainapp.views import index, registration, catalogs, test, get_question
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('catalog/', catalogs, name='catalog'),
    path('catalog/<int:pk>/', catalogs, name='catalog'),
    path('catalog/test/<int:pk>/', test, name='test'),
    path('catalog/test/<int:test_id>/questions/<int:pk>/', get_question, name='question'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration, name='registration'),
]
