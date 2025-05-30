📄 [English version](README.en.md)
# 🧉 AMATE

Sitio web tipo blog informativo sobre el mate argentino. Desarrollado con Django, AMATE permite crear publicaciones, gestionar productos, registrarse como usuario, y más.

🔗 **Demo online:** [juanbaquiroga1.pythonanywhere.com](https://juanbaquiroga1.pythonanywhere.com/home)

---

## 🚀 Tecnologías utilizadas

- **Backend:** Python + Django
- **Frontend:** HTML y CSS
- **Base de datos:** SQLite

---

## 🧪 Instalación local

```bash
git clone https://github.com/juanbaquiroga/AMATE.git
cd AMATE
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Luego accedé a: [localhost:8000/home/](http://localhost:8000/home/)

---

## 📌 Funcionalidades principales

### 🏠 Home (`/home/`)
- Listado de publicaciones.
- Crear, editar y eliminar publicaciones (CRUD).
- Vista detallada por publicación.

### 🛍 Productos (`/productos/`)
- Listado de productos disponibles.
- Buscador integrado.
- Vista detallada, edición y eliminación.

### 🧾 Categorías
- Listado de categorías disponibles.
- Crear, editar y eliminar categorías.

### 👤 Autenticación
- Registro y login de usuarios.
- Edición de perfil (foto, teléfono, web).
- Modificación de usuario (email, username).
- Logout.

### ℹ️ About Us
- Información sobre el propósito del sitio.

---

## 🗃 Estructura del proyecto

```
AMATE/
├── amate/            # Configuración principal del proyecto Django
├── blog/             # Aplicación principal (posts, productos, usuarios)
├── templates/        # HTML templates
├── static/           # Archivos estáticos (CSS, imágenes)
├── db.sqlite3        # Base de datos SQLite
└── manage.py
```

---

## 🙋 Sobre el proyecto

Este proyecto fue realizado como práctica para aplicar conocimientos de Django y desarrollo web full stack. A través de este blog, se explora la cultura del mate argentino mientras se implementan funcionalidades clave como autenticación, panel de usuario, y gestión de contenido.

---

## 📫 Contacto

Juan Bautista Quiroga  
📧 juanbaquiroga@gmail.com  
🌐 [Portfolio](https://juanbaquiroga.vercel.app) | [LinkedIn](https://linkedin.com/in/juanbaquiroga) | [GitHub](https://github.com/juanbaquiroga)
