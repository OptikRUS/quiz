from django.urls import path

from quizapp.views import catalogs, test, get_question

app_name = 'quizapp'

urlpatterns = [

    path('', catalogs, name='catalog'),
    path('<int:pk>/', catalogs, name='catalog'),
    path('test/<int:pk>/', test, name='test'),
    path('test/<int:test_id>/questions/<int:pk>/', get_question, name='question'),
]
