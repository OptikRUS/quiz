from django.db import models
from django.template.defaultfilters import truncatewords
from django.contrib.auth.models import User

from model_utils.managers import InheritanceManager


class QuizCategory(models.Model):
    name = models.CharField('название категории', max_length=64, unique=True)
    description = models.TextField('описание', blank=True, null=True)

    class Meta:
        verbose_name = 'категория тестов'
        verbose_name_plural = 'категории тестов'

    def __str__(self):
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE, verbose_name='категория')
    title = models.CharField('название теста', max_length=64, unique=True)
    description = models.TextField('описание', blank=True, null=True)

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return self.title


class Question(models.Model):
    CHOICES_TYPE = [
        ("1", "Ответ с выбором одного варианта"),
        ("2", "Ответ с выбором нескольких вариантов"),
    ]

    objects = InheritanceManager()

    test = models.ForeignKey(
        verbose_name="Тесты",
        to=Quiz,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    description = models.TextField(verbose_name="Описание")
    type_question = models.CharField(
        verbose_name="Тип вопроса", choices=CHOICES_TYPE, max_length=2
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
        unique_together = (("test", "description", "type_question"),)

    def __str__(self):
        return f"{self.description}"

    @property
    def short_description(self):
        return truncatewords(self.description, 5)


class Answer(models.Model):
    text = models.TextField(verbose_name="Ответ")
    question = models.ForeignKey(verbose_name="Вопрос",  to=Question, on_delete=models.CASCADE, related_name="answers")
    user = models.ForeignKey(verbose_name="Пользователь", to=User, blank=True, null=True, on_delete=models.CASCADE,
                             related_name="user_answers",)
    is_admin = models.BooleanField(default=True)
    is_right = models.BooleanField(verbose_name="Правильный ответ", default=False)

    class Meta:
        ordering = ['?']
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        unique_together = (("text", "question", "user", "is_admin"),)

    def __str__(self):
        return f"{self.text}"

    @property
    def short_text(self):
        return truncatewords(self.text, 5)
