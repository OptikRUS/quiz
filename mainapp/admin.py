from django.contrib import admin

from mainapp.models import QuizCategory, Quiz, Question, Answer


@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class QuestionAdminInline(admin.StackedInline):
    model = Question
    extra = 0


class AnswerAdminInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('description', 'type_question')
    search_fields = ('description', )
    inlines = (AnswerAdminInline, )


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):

    list_display = ('title', 'category')
    list_filter = ('category',)
    inlines = (QuestionAdminInline, )

    search_fields = ('title', )
