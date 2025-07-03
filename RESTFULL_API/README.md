# Sensor Data API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-orange.svg)

Una API RESTful para gestionar datos de sensores, permitiendo la creación de dispositivos, el registro de datos con cálculos automatizados, y la consulta, actualización y eliminación de información. Construida con FastAPI y SQLAlchemy, utilizando PostgreSQL como base de datos.

---

## 🚀 Características

* **Gestión de Dispositivos:**
    * Crea nuevos dispositivos.
    * Actualiza nombres de dispositivos existentes.
* **Gestión de Datos de Elementos:**
    * Registra datos de elementos (ej. lecturas de sensores) asociados a un dispositivo.
    * Calcula automáticamente promedios (antes y después de normalización) y el tamaño de los datos al momento del registro.
    * Consulta todos los elementos con filtros avanzados (fecha de creación, promedios, tamaño de datos).
    * Obtén un elemento específico por su ID.
    * Elimina elementos por su ID.
* **Base de Datos:** PostgreSQL.
* **Documentación Interactiva:** Generación automática de documentación OpenAPI (Swagger UI/ReDoc).

---

## 🛠️ Requisitos Previos

Antes de empezar, asegúrate de tener instalado lo siguiente:

* **Python 3.9+**
* **pip** (Administrador de paquetes de Python)
* **PostgreSQL** (Servidor de base de datos)

---

## ⚙️ Configuración del Entorno

1.  **Clona el Repositorio:**
    ```bash
    git clone https://github.com/jj131204/Prueba-Tecnica---IMEXHS-Desarrollador-III
    cd Prueba-Tecnica---IMEXHS-Desarrollador-III/RESTFULL_API
    ```

2.  **Crea y Activa un Entorno Virtual:**
    Es una buena práctica para gestionar las dependencias del proyecto.
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instala Dependencias:**
    Crea un archivo `requirements.txt` con estas librerías (si no lo tienes ya) y luego instálalas:
    ```
    # requirements.txt
    fastapi==0.111.0
    uvicorn==0.30.1
    sqlalchemy==2.0.30
    psycopg2-binary==2.9.9
    pydantic==2.7.4
    # Agrega cualquier otra dependencia que tengas
    ```
    Luego instala:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura la Base de Datos:**
    * Asegúrate de tener un servidor **PostgreSQL** corriendo.
    * Crea una base de datos con el nombre que usarás (ej. `sensor_db`).
    * Modifica el archivo **`database.py`** con tus credenciales de PostgreSQL:

        ```python
        # database.py
        DB_USER = "postgres"
        DB_PASSWORD = "admin123"
        DB_HOST = "127.0.0.1"
        DB_PORT = "5432"
        DB_NAME = "sensor_db"

        DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        
        ```

---

## ▶️ Ejecutar la Aplicación

Desde la raíz del proyecto y con tu entorno virtual activado:

```bash
uvicorn main:app --reload


## 📖 Documentación de la API

Una vez que la aplicación esté corriendo, puedes acceder a la documentación interactiva de la API en tu navegador:

    * Swagger UI: http://127.0.0.1:8000/docs

    * ReDoc: http://127.0.0.1:8000/redoc

Esta documentación te permite probar directamente los endpoints desde la interfaz, ver los esquemas de datos y las posibles respuestas.