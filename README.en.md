---

# 🧉 AMATE (English)

Informative blog-style website about Argentine mate. Built with Django, AMATE allows users to create posts, manage products, register, and more.

🔗 **Live demo:** [juanbaquiroga1.pythonanywhere.com](https://juanbaquiroga1.pythonanywhere.com/home)

---

## 🚀 Technologies used

- **Backend:** Python + Django  
- **Frontend:** HTML and CSS  
- **Database:** SQLite  

---

## 🧪 Local setup

```bash
git clone https://github.com/juanbaquiroga/AMATE.git
cd AMATE
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then visit: [localhost:8000/home/](http://localhost:8000/home/)

---

## 📌 Main features

### 🏠 Home (`/home/`)
- Post list.
- Create, edit, and delete posts (CRUD).
- Post detail view.

### 🛍 Products (`/productos/`)
- Product list.
- Integrated search bar.
- Product detail view, edit and delete.

### 🧾 Categories
- View all product categories.
- Create, edit and delete categories.

### 👤 Authentication
- User sign up and login.
- Edit profile (photo, phone, website).
- Edit user info (username and email).
- Logout.

### ℹ️ About Us
- Page with information about the project’s purpose.

---

## 🗃 Project structure

```
AMATE/
├── amate/            # Django project config
├── blog/             # Main app (posts, products, users)
├── templates/        # HTML templates
├── static/           # Static files (CSS, images)
├── db.sqlite3        # SQLite database
└── manage.py
```

---

## 🙋 About the project

This project was built as a full stack Django practice to apply core concepts like CRUD operations, authentication, user profiles, and database relationships, while sharing knowledge about Argentina's mate culture.

---

## 📫 Contact

Juan Bautista Quiroga  
📧 juanbaquiroga@gmail.com  
🌐 [Portfolio](https://juanbaquiroga.vercel.app) | [LinkedIn](https://linkedin.com/in/juanbaquiroga) | [GitHub](https://github.com/juanbaquiroga)
