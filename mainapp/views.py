from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from mainapp.models import Quiz, QuizCategory
from quiz.forms import UserRegistrationForm, QuestionForm


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


@login_required
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
    test_ = Quiz.objects.filter(id=test_id).first()
    questions = test_.questions.all()
    max_page = len(questions)
    question = test_.questions.all()[pk]

    context = {
        'title': 'Вопросы',
        'question': question,
        'description': question.description,
        'answers': question.answers.all(),
        'test_id': question.test_id,
        'pk': pk + 1,
        'max_page': max_page,
    }
    return render(request, 'mainapp/test/question.html', context)

