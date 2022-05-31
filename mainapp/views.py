from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from mainapp.models import Quiz, QuizCategory, Answer
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


# class AdminUserCreateView(CreateView):
#     model = User
#     template_name = 'registration/registration.html'
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('login')
#     title = 'Регистрация'
#     success_message = 'Пользователь успешно создан!'


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
    hold = (test_id, pk - 1)

    if request.method == "POST":
        form = QuestionForm(request.POST)
    else:
        form = QuestionForm()

    form.user_answer_instance()

    if form.is_valid():
        quiz = get_object_or_404(Quiz, pk=test_id)

        try:
            question = quiz.questions.all()[pk]
        except IndexError:
            results = form.instance
            results.pop('csrfmiddlewaretoken')
            answers_list = [i[0] for i in results.values()]
            count_rights = Answer.objects.filter(question_id__in=quiz.questions.all()).filter(is_right=1).count()
            # count_wrongs = Answer.objects.filter(question_id__in=quiz.questions.all()).filter(is_right=0).count()
            context = {
                'title': 'Результаты',
                'questions_count': quiz.questions.count(),
                'total_answers': len(results),
                'rights': answers_list.count('True'),
                'wrongs': answers_list.count('False'),
                'all_rights': int(answers_list.count('True') / count_rights * 100),
            }
            form.clean_instance()
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
        return render(request, 'mainapp/test/question.html', context)
    else:
        return HttpResponseRedirect(reverse_lazy('question', args=hold))
