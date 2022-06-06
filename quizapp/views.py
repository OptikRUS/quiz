from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from quizapp.models import Quiz, QuizCategory, Answer
from quizapp.forms import QuestionForm

from quiz.forms import UserRegistrationForm


def index(request):
    return render(request, 'quizapp/index.html', {'title': 'Главная'})


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
    return render(request, 'quizapp/tests.html', context)


@login_required
def test(request, pk):
    quiz = Quiz.objects.filter(id=pk).first()
    questions = quiz.questions.all()
    try:
        question = questions.first()
        question_pk = question.pk
    except (IndexError, AttributeError):
        question = 'нет вопросов'
        question_pk = 0

    context = {
        'title': quiz.title,
        'question': question,
        'category': quiz.category.name,
        'description': quiz.description,
        'questions_count': questions.count(),
        'test_id': pk,
        'question_pk': question_pk,
        'pk': 0,
    }
    return render(request, 'test/index.html', context)


@login_required
def get_question(request, test_id, pk):

    if request.method == "POST":
        form = QuestionForm(request.POST)
    else:
        form = QuestionForm()

    if form.is_valid():
        pk += 1

    form.user_answer_instance()
    quiz = Quiz.objects.get(pk=test_id)

    try:
        question = quiz.questions.all()[pk]
    except IndexError:
        return get_results(request, test_id, form)

    context = {
        'title': 'Вопросы',
        'question': question,
        'description': question.description,
        'answers': question.answers.all(),
        'test_id': test_id,
        'pk': pk,
        'form': form,
    }

    return render(request, 'test/question.html', context)


def get_results(request, test_id, form):
    quiz = Quiz.objects.get(pk=test_id)
    results = form.instance
    results.pop('csrfmiddlewaretoken')
    answers_list = [i[0] for i in results.values()]
    count_rights = Answer.objects.filter(question_id__in=quiz.questions.all()).filter(is_right=1).count()
    context = {
        'title': 'Результаты',
        'questions_count': quiz.questions.count(),
        'total_answers': len(results),
        'rights': answers_list.count('True'),
        'wrongs': answers_list.count('False'),
        'all_rights': int(answers_list.count('True') / count_rights * 100),
    }
    form.clear_instance()
    return render(request, 'test/result.html', context)
