# Killa TODO list

Backend de prueba tecnica *Killa* TODO list
Este proyecto es una aplicación de gestión de tareas (TODO list) construida con Django y Django REST Framework. Proporciona una API RESTful para crear, leer, actualizar y eliminar tareas.

## Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu entorno:

- Python 3.x
- pip (gestor de paquetes de Python)

### Versiones utilizadas

* Python 3.14.2
* Django 6.0
* Sqlite3


## Ejecucion
* Crear entorno virtual
``` bash
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate     # En Windows
```

* Instalar dependencias
```bash
    pip install -r requirements.txt
```

* Realizar Migraciones
```bash
    python manage.py makemigrations
    python manage.py migrate
```

* Iniciar el servidor
```bash
    python manage.py runserver
```