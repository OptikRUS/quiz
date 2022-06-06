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
* Список всех зависимостей должен храниться в __requirements.txt__, соответственно можно установить их командой ```pip install -r requirements.txt```. 
* Разработка должны вестись в __virtualenv__, но сама директория с __virtualenv__ должна быть добавлена в __.gitignore__. 
* Настройки должны храниться в __settings.py__, но также, при наличии __settings_local.py__ в той же директории, настройки из __settings_local.py__ должны переопределять настройки в __settings.py__. 
Т.е. если есть файл __settings_local.py__, то определенные в нем параметры имеют больший приоритет. 
Сам файл __settings_local.py__ добавляется в __.gitignore__. Таким образом у каждого девелопера и на бета сервере можно использовать кастомные настройки, например для соединения с БД. 
* Должен работать один из способов создания структуры БД. Встроенный manage.py syncdb или миграции через South (будет плюсом). 
* По фронтенду требований никаких не предъявляется. Интерфейс на твое усмотрение и он не будет оцениваться. Можно использовать любимый фреймворк или, например, воспользоваться Twitter Bootstrap.

<details>
  <summary>Скриншоты проекта</summary>

[![Регистрация пользователя](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/1.png "Регистрация пользователя")]()
[![Категория тестов](https://raw.githubusercontent.com/OptikRUS/quiz/0de4156f3d9717d3a832824b6f50e0352d8ab1fc/images/2.png "Категория тестов")]()
[![Страница теста](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/3.png "Страница теста")]()
[![Вопросы к тесту](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/4.png "Вопросы к тесту")]()
[![Вопросы к тесту](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/5.png "Вопросы к тесту")]()
[![Результаты теста](https://raw.githubusercontent.com/OptikRUS/quiz/3e405ef786eac72dd4db00cfb14b6b83596b69f4/images/6.png "Результаты теста")]()
[![Админка тесты](https://raw.githubusercontent.com/OptikRUS/quiz/aaf027dd9893ecb9f97216236f95d69dc5912128/images/7.png "Админка тесты")]()
[![Админка вопросы](https://raw.githubusercontent.com/OptikRUS/quiz/aaf027dd9893ecb9f97216236f95d69dc5912128/images/8.png "Админка вопросы")]()
  
</details>

## Запуск проекта
* Клонировать репозиторий: ```https://github.com/OptikRUS/quiz```
* Установить зависимости: ```pip install -r requirements.txt```
* Сделать миграции:
  * ```python manage.py makemigrations```
  * ```python manage.py migrate```
* Создать суперпользователя ```python manage.py createsuperuser```
* Запустить проект ```python manage.py runserver```
