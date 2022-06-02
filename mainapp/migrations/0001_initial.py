# Generated by Django 4.0.4 on 2022-06-02 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория тестов',
                'verbose_name_plural': 'категории тестов',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='название теста')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.quizcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('type_question', models.CharField(choices=[('1', 'Ответ с выбором одного варианта'), ('2', 'Ответ с выбором нескольких вариантов')], max_length=2, verbose_name='Тип вопроса')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='mainapp.quiz', verbose_name='Тесты')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'unique_together': {('test', 'description', 'type_question')},
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Ответ')),
                ('is_admin', models.BooleanField(default=True)),
                ('is_right', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='mainapp.question', verbose_name='Вопрос')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ['?'],
                'unique_together': {('text', 'question', 'user', 'is_admin')},
            },
        ),
    ]
