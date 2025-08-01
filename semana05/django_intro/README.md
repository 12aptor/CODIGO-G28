# Django

## Crear un proyecto 1/2

```bash
mkdir django_intro
cd django_intro
```

## Crear un entorno virtual

```bash
python -m venv venv
source venv/Scripts/activate
```

## Instalar dependencias

```bash
pip install Django
```

## Crear el proyecto 2/2

```bash
django-admin startproject django_intro .
```

## Iniciar el servidor

```bash
python manage.py runserver
```

## Aplicar la migración inicial

```bash
python manage.py migrate
```

## Crear un superusuario

```bash
python manage.py createsuperuser
```

## Crear una aplicación

```bash
python manage.py startapp almacen
```

## Ejecutar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```