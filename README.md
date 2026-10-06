# 📚 Biblioteca Django - Sistema de Gestión y Catálogo

Sistema web institucional y de gestión para una biblioteca, desarrollado con Python, Django y Bootstrap 5. El proyecto implementa un flujo completo de gestión con una interfaz limpia, minimalista y responsive, complementado con un sistema robusto de autenticación y una **API RESTful completa** con soporte para sincronización offline.

<img src="image.png" alt="Vista del proyecto" width="800">

## ✨ Características Principales
- 📊 **Dashboard Principal (`/`):** Panel de control centralizado con métricas clave (total de libros, libros disponibles y total de autores) y accesos directos.
- 📖 **Catálogo de Libros y Autores:** Listado y gestión completa de libros, géneros, estados y autores asociados.
- 🔌 **API RESTful (`/api/`):** Endpoints seguros construidos con Django REST Framework para consumo externo o aplicaciones móviles.
- 🔄 **Sincronización Offline (`/api/sync/`):** Funcionalidad especial para recibir y validar cargas masivas de datos recolectados sin conexión.
- 🛡️ **Seguridad Avanzada:** Autenticación de sesiones tradicionales para la web y protección mediante **JSON Web Tokens (JWT)** para todos los endpoints de la API.

---

## 🛠️ Tecnologías Utilizadas

*   **Backend**: Python 3.13, Django 4.2, Django REST Framework, SimpleJWT
*   **Base de Datos**: MySQL (XAMPP)
*   **Frontend**: HTML5, CSS3, Bootstrap 5, Google Fonts

---

## 📂 Estructura del Sitio

*   **Inicio (`/`)**: Dashboard general con estadísticas y accesos rápidos.
*   **Catálogo de Libros (`/catalogo/`)**: Tabla con los libros registrados, códigos, géneros, años, estados y autor.
*   **Autores (`/autores/`)**: Listado de autores registrados en el sistema.
*   **Acceso (`/accounts/login/`)**: Inicio de sesión exclusivo para administradores y personal autorizado.

---

📂 Estructura de Endpoints de la API
Si deseas interactuar con la API RESTful (por ejemplo, mediante Postman), estas son las rutas principales disponibles:

1. **Autenticación (JWT):**
   - Obtener Token: `POST /api/token/` (Envía `username:inacap` y `password:inacap123` en formato JSON para recibir tu token de acceso).
   - Refrescar Token: `POST /api/token/refresh/`

2. **Gestión de Recursos (Requieren Header: `Authorization: Bearer`):**
   - Libros (CRUD completo): `GET`, `POST`, `PUT`, `DELETE` en `/api/libros/`
   - Autores (Listar): `GET` en `/api/autores/`
   - Sincronización Offline: `POST /api/sync/` (Envía un arreglo JSON con múltiples registros para almacenamiento masivo seguro).
   
---

## 🚀 Instalación y Puesta en Marcha

1. **Clonar el repositorio:**
git clone [https://github.com/bellybelly21/biblioteca-django.git](https://github.com/bellybelly21/biblioteca-django.git)
cd biblioteca-django
   
2. **Crear y activar un entorno virtual:**
python -m venv venv
# En Windows:
venv\Scripts\activate

3. **Instalar dependencias:**
pip install django

4. **Aplicar migraciones a la base de datos:**
python manage.py makemigrations
python manage.py migrate

5. **Crear un superusuario (para acceder a las funciones de creación, edición y eliminación):**
python manage.py createsuperuser

6. **Ejecutar el servidor de desarrollo:**
python manage.py runserver

Luego, ingresa desde tu navegador a: http://127.0.0.1:8000/


🎯 Objetivo
El objetivo del proyecto es desarrollar una aplicación web funcional utilizando Django, superando el panel de administración tradicional para ofrecer una interfaz pública respaldada por un sistema seguro de autenticación de sesiones y gestión de datos relacionales (Libros y Autores).

📄 Licencia
Proyecto desarrollado con fines académicos y educativos.

