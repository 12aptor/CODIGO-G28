# Migraciones

## Instalación

```bash
pip install flask-migrate
```

## Ejecutación

```bash
flask db init # Inicializar la migración (Solo la primera vez)
flask db migrate -m "Descripción de la migración" # Crear las migraciones
flask db upgrade # Ejecutar las migraciones
```