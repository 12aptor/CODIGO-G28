# Django Barbershop

## Crear el proyecto

```bash
mkdir django_barbershop
cd django_barbershop
python -m venv venv
source venv/Scripts/activate # Windows
source venv/bin/activate # MacOS / Linux
```

## Instalar dependencias

```bash
pip install Django djangorestframework psycopg2-binary python-dotenv drf-spectacular django-cors-headers
# ó
pip install -r requirements.txt
```

## Variables de entorno

```bash
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

## Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

## Iniciar el servidor

```bash
python manage.py runserver
```

# Tests

## Instalar dependencias

```bash
pip install pytest pytest-django pytest-cov Faker
```

## Configuración `pytest.ini`

```ini
[pytest]
DJANGO_SETTINGS_MODULE = django_barbershop.settings
python_files = tests.py test_*.py *_tests.py
filterwarnings = ignore::DeprecationWarning
```