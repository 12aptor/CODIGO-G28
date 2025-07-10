# Entornos virtuales 🤠

## ¿Qué es un entorno virtual?
Es una herramienta que nos permite crear un entorno de desarrollo aislado del sistema principal. Esto permite instalar las dependencias necesarias para nuestro proyecto sin afectar a otros proyectos.

## Crear un entorno virtual

```bash
python -m venv "nombre-del-entorno"
```

## Activar un entorno virtual

```bash
# Windows cmd
nombre-del-entorno\Scripts\activate
# Windows Git Bash
source nombre-del-entorno/Scripts/activate

# Linux/MacOS
source nombre-del-entorno/bin/activate
```

## Desactivar un entorno virtual

```bash
deactivate
```

## Instalar dependencias

```bash
pip install "nombre-de-la-dependencia"
```

## Listar dependencias

```bash
pip freeze
pip list
```

## Exportar dependencias

```bash
pip freeze > requirements.txt
```

## Instalar dependencias desde un archivo

```bash
pip install -r requirements.txt
```