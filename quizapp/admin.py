from django import forms
from django.contrib import admin

from quizapp.models import QuizCategory, Quiz, Question, Answer


class QuizAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = []


class QuestionAdminForm(QuizAdminForm):
    class Meta:
        model = Question
        exclude = []


class AnswerAdminForm(forms.models.BaseInlineFormSet):
    def clean(self):
        if self.cleaned_data:
            try:
                right_list = [form.cleaned_data['is_right'] for form in self.forms]
            except KeyError:
                raise forms.ValidationError("Выбери правильный/неправильный ответ")
            if len(set(right_list)) == 1:
                raise forms.ValidationError("Выбери правильный/неправильный ответ")


class AnswerAdminInline(admin.TabularInline):
    model = Answer
    formset = AnswerAdminForm
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
