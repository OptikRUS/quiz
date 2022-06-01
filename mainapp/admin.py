from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from mainapp.models import QuizCategory, Quiz, Question, Answer


class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = []

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(), required=False,
        label="вопросы", widget=FilteredSelectMultiple(verbose_name="вопросы", is_stacked=False))


class AnswerAdminForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = []


@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class QuestionAdminInline(admin.StackedInline):
    model = Question
    extra = 0


class AnswerAdminInline(admin.TabularInline):
    model = Answer
    extra = 0
    form = AnswerAdminForm


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'type_question')
    search_fields = ('description', )
    inlines = (AnswerAdminInline, )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = ('title', 'category')
    list_filter = ('category',)
    inlines = (QuestionAdminInline, )
    search_fields = ('title', )
