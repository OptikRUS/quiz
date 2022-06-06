from django.contrib import admin
from django.urls import path, include

from quizapp.views import index, registration


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('catalog/', include('quizapp.urls', namespace='catalog')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', registration, name='registration'),
]
