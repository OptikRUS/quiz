from django.db import models


class TestCategory(models.Model):
    name = models.CharField('название категории', max_length=64, unique=True)
    description = models.TextField('описание', blank=True, null=True)

    class Meta:
        verbose_name = 'категория тестов'
        verbose_name_plural = 'категории тестов'

    def __str__(self):
        return self.name


class Test(models.Model):
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, verbose_name='категория')
    title = models.CharField('название теста', max_length=64, unique=True)
    description = models.TextField('описание', blank=True, null=True)

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return self.title
