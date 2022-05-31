from django.contrib import admin

from mainapp.models import QuizCategory, Quiz, Question, Answer
from django import forms


@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class QuestionAdminInline(admin.TabularInline):
    model = Question
    extra = 0


class AnswerAdminInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuizAdminForm(forms.ModelForm):

    answers = Answer.objects.all()

    class Meta:
        model = Quiz
        exclude = []


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'type_question')
    search_fields = ('description', )
    inlines = (AnswerAdminInline, )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    forms = QuizAdminForm

    list_display = ('title', 'category')
    list_filter = ('category',)
    inlines = (QuestionAdminInline, )

    search_fields = ('title', )
