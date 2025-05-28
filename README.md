# Weather App (Django)

## Описание

В этом тестовом задании используется Django 

## Реализовано
- Django view для обработки GET-запроса с параметром города (`get_weather` в `views.py`).
- Использование внешних API: геокодинг и получение погоды через Open-Meteo.
- HTML-шаблон с автодополнением городов (Awesomplete, JS).
- Простые тесты для проверки работы представления (`tests.py`).
- Чистый и современный UI (CSS в шаблоне).

## Использованные технологии
- Python 3, Django
- requests (для работы с внешними API)
- Awesomplete (автодополнение городов на фронте)
- HTML5, CSS3, JavaScript (минимально)

## Как запустить
1. Клонируйте репозиторий и перейдите в папку проекта:
    ```
    git clone https://github.com/Pro100Sergosha/Test-task.git 
    ```
2. Создайте виртуальное окружение:
   ```sh
   python -m venv venv
   ```
3. Активируйте виртуальное окружение:
    ```
    venv/scripts/activate
    ```
3. Установите зависимости:
   ```sh
   pip install -r requrements.txt
   ```
4. Выполните миграции:
   ```sh
   python manage.py migrate
   ```
5. Запустите сервер:
   ```sh
   python manage.py runserver
   ```
6. Откройте в браузере: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## Тесты
Для запуска тестов:
```sh
python manage.py test weather
```

---

**Структура проекта:**
- `weather/` — основное приложение (views, urls, tests, templates)
- `weather_app/` — настройки Django
- `templates/home.html` — основной шаблон

**P.S.** Для работы автодополнения требуется интернет (используется внешний JS и API).

