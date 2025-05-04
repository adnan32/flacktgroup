# 🧾 Product Record System

A simple Django-based web application for managing product records. Users can view, add, and edit products with attributes name, part number, size (in mm), and color.

## 🚀 Features

- List all products
- Add new products
- Edit existing products

## 🛠️ Tech Stack

- Python 3.x
- Django 4.2.x
- SQLite (default dev database)
- HTML5 + Bootstrap 5 (for frontend)

## ⚙️ Setup Instructions

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/product-record-system.git
cd product-record-system
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Then open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---


## 🗃 Project Structure

```
product_record_system/
├── manage.py
├── products/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   └── products/
│   │       ├── product_list.html
│   │       └── product_form.html
├── product_record_system/
│   ├── settings.py
│   ├── urls.py
```