from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.views.generic import ListView

from mainapp.models import Quiz, QuizCategory, Question, Answer
from quiz.forms import UserRegistrationForm


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Регистрация прошла успешно.')
            return HttpResponseRedirect(reverse('login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'регистрация',
        'form': form
    }
    return render(request, 'registration/registration.html', context)


def catalogs(request, pk=None):
    if pk:
        tests = Quiz.objects.filter(category_id=pk)
    else:
        tests = Quiz.objects.all()
    context = {
        'title': 'Тесты',
        'tests': tests,
        'catalog': QuizCategory.objects.all(),
    }
    return render(request, 'mainapp/tests.html', context)


def test(request, pk):
    test_ = Quiz.objects.filter(id=pk).first()
    questions = test_.questions.all()
    context = {
        'title': test_.title,
        'category': test_.category.name,
        'description': test_.description,
        'questions_count': questions.count(),
        'questions': questions,
        'test_id': pk,
    }
    return render(request, 'mainapp/test/index.html', context)


# def get_question(request, test_id, pk):
#
#     pass


# class ListQuestions(ListView):
#     model = Question
#     template_name = 'mainapp/test/question.html'
#     paginate_by = 1


# def question(request, pk, page):
#     questions = Question.objects.filter(test_id=pk)
#     paginator = Paginator(questions, len(questions))
#     try:
#         questions_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         questions_paginator = paginator.page(1)
#     except EmptyPage:
#         questions_paginator = paginator.page(paginator.num_pages)
#     context = {
#         'title': 'вопросы',
#         'questions': questions_paginator,
#     }
#     return render(request, 'mainapp/test/question.html', context)
