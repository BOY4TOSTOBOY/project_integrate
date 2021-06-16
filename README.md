# Шаблон для проекта

**Используются:**
- Python 3.7+
- Django 3.0+
- Celery 5.0+
- Channels 3+

Проект для организации бэкенд сервера и поддержки websockets


## Начиная

Ссылки для доступа к репозиторию:

SSH clone URL: ssh://git@git.jetbrains.space/meotyda/klub-prepodavateley/resource-server.git
HTTPS clone URL: https://git.jetbrains.space/meotyda/klub-prepodavateley/resource-server.git

Эти инструкции позволят вам запустить копию проекта на локальном компьютере для
в целях разработки и тестирования.


## Подготовка

Что нужно для установки программного обеспечения и как их установить.

Создание virtualenv:

```bash
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt

```

## Генерация документации

Команду `sphinx-apidoc` нужно выполнять если добавляются новые модули в систему.

```bash
python3 -m venv ./venv
source venv/bin/activate
cd docs
sphinx-apidoc -o ./source ../src # Если требуется
make html

```

После выполнения команды `make html` набор html файлов находиться в директории `docs/build/`
При необходимости можно выполнить сборку в PDF файл.

## Запуск веб-сервера разработки

```bash
source venv/bin/activate
cd src/
python3 manage.py runserver

```

#### Приминение миграций и fixtures
Фикстуры храняться в директории приложения

```bash
source venv/bin/activate
cd src/
python3 manage.py migrate
python3 manage.py loaddata fixtures/auth.json

python3 manage.py loaddata --app snippets initial_data

```


#### Запуск celery worker

```bash
source venv/bin/activate
cd src/
celery -A system worker -l INFO

```


## Запуск юнит-тестирования

```bash
source venv/bin/activate
cd src/
python3 manage.py test 

```

#### тестирование с покрытием кода

```bash
source venv/bin/activate
cd src/
coverage run --source='.' manage.py test

```

#### проверка качества кода

```bash
isort --check-only src
flake8 --ignore=E501,F401,E128,E402,E731,F821 src

```


## Развертывание

Дополнительные примечания о том, как развернуть это в производственной системе.


## Дополнительные ресурсы

Ссылки на внешние ресурсы для этого проекта, такие как CI-сервер, трекер задач и т.Д.