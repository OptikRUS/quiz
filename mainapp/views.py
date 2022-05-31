from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from mainapp.models import Quiz, QuizCategory
from mainapp.templates.mainapp.forms import QuestionForm
from quiz.forms import UserRegistrationForm


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'Главная'})


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


@login_required
def catalogs(request, pk=0):
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


@login_required
def test(request, pk):
    test_ = Quiz.objects.filter(id=pk).first()
    questions = test_.questions.all()
    try:
        question = questions[0]
        question_pk = question.pk
    except IndexError:
        question = 'нет вопросов'
        question_pk = 0

    context = {
        'title': test_.title,
        'question': question,
        'category': test_.category.name,
        'description': test_.description,
        'questions_count': questions.count(),
        'test_id': pk,
        'question_pk': question_pk,
        'pk': 0,
    }
    return render(request, 'mainapp/test/index.html', context)


@login_required
def get_question(request, test_id, pk=0):
    if request.method == "POST":
        form = QuestionForm(request.POST)
    else:
        form = QuestionForm()

    print(form.is_valid())

    quiz = Quiz.objects.filter(id=test_id).first()

    try:
        question = quiz.questions.all()[pk]
    except IndexError:
        context = {
            'title': 'Результаты',
        }
        return render(request, 'mainapp/test/result.html', context)
    else:
        pk += 1

    context = {
        'title': 'Вопросы',
        'question': question,
        'description': question.description,
        'answers': question.answers.all(),
        'test_id': question.test_id,
        'pk': pk,
        'form': form,
    }
    if form.is_valid():
        return render(request, 'mainapp/test/question.html', context)
    print(form.errors)
    return HttpResponseRedirect(reverse('question', args=(context['test_id'], context['pk'] - 2)))
