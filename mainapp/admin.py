from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from mainapp.models import QuizCategory, Quiz, Question, Answer


class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = []


class QuestionAdminForm(QuizAdminForm):
    class Meta:
        model = Question
        exclude = []


class AnswerAdminForm(QuizAdminForm):
    class Meta:
        model = Answer
        exclude = []


class AnswerAdminInline(admin.TabularInline):
    model = Answer
    form = AnswerAdminForm
    extra = 0
    fields = ('text', 'is_right')


class QuestionAdminInline(admin.StackedInline):
    model = Question
    form = QuestionAdminForm
    extra = 0
    inlines = (AnswerAdminInline,)


@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'type_question', )
    list_filter = ('test',)
    search_fields = ('description', )
    inlines = (AnswerAdminInline, )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    form = QuizAdminForm

    list_display = ('title', 'category')
    list_filter = ('category',)
    inlines = (QuestionAdminInline, )
    search_fields = ('title', )
