# Тестовое задание для Fortech
___
Нужно сделать простой сервис проведения тестирования по каким-либо темам. 
Т.е. есть тесты с вариантами ответов, один или несколько вариантов должны быть правильными. 
Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат.
___
## Функциональные части сервиса:
* Регистрация пользователей
* Аутентификация пользователей
* Зарегистрированные пользователи могут 
  * Проходить любой из тестовых наборов 
  * Последовательный ответ на все вопросы, каждый вопрос должен выводится на новой странице с отправкой формы (перескакивать через тесты или оставлять неотмеченными нельзя)
  * После завершения тестирования смотреть результат:
    * количество правильных/неправильных ответов 
    * процент правильных ответов 
* Админка. Стандартная админка Django. Разделы:
  * Стандартный раздел пользователей 
  * Раздел с наборами тестов 
  * Возможность на странице набора тестов добавлять вопросы/ответы к вопросам/отмечать правильные ответы 
  * Валидация на то, что должен быть хотя бы 1 правильный вариант 
  * Валидация на то, что все варианты не могут быть правильными 
  * Удаление вопросов/вариантов ответов/изменение правильных решений при редактировании тестового набора
___
* Код в репозитории на GitHub. 
* Список всех зависимостей должен храниться в __requirements.txt__, соответственно можно установить их командой pip install -r requirements.txt. 
* Разработка должны вестись в virtualenv, но сама директория с virtualenv должна быть добавлена в .gitignore. 
* Настройки должны храниться в settings.py, но также, при наличии settings_local.py в той же директории, настройки из settings_local.py должны переопределять настройки в settings.py. Т.е. если есть файл settings_local.py, то определенные в нем параметры имеют больший приоритет. 
Сам файл settings_local.py добавляется в .gitignore. Таким образом у каждого девелопера и на бета сервере можно использовать кастомные настройки, например для соединения с БД. 
* Должен работать один из способов создания структуры БД. Встроенный manage.py syncdb или миграции через South (будет плюсом). 
* По фронтенду требований никаких не предъявляется. Интерфейс на твое усмотрение и он не будет оцениваться. Можно использовать любимый фреймворк или, например, воспользоваться Twitter Bootstrap.

<details>
  <summary>Скриншоты проекта</summary>

[![Регистрация пользователя](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/1.png)]()
[![Категория тестов](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/2.png)]()
[![Страница теста](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/3.png)]()
[![Вопросы к тесту](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/4.png)]()
[![Вопросы к тесту](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/5.png)]()
[![Результаты теста](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/6.png)]()
  
</details>

## Запуск проекта
* Клонировать репозиторий: ```https://github.com/OptikRUS/quiz```
* Установить зависимости: ```pip install -r requirements.txt```
* Сделать миграции:
  * ```python manage.py makemigrations```
  * ```python manage.py migrate```
* Создать суперпользователя ```python manage.py createsuperuser```
* Запустить проект ```python manage.py runserver```
