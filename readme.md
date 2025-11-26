# 🦊 Foxvoid

> The official ecosystem platform for the **[Fantasy Craft](https://github.com/ikigami0513/fantasy_craft)** game engine.

![Foxvoid Banner](https://placehold.co/1200x300/1a1a1a/ff6b00?text=Foxvoid+Platform&font=montserrat)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

[![Django](https://img.shields.io/badge/Django-5.0-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3670A0?logo=python&logoColor=white)](https://www.python.org/)

**Foxvoid** is a monolithic Django application designed to serve as the central hub for the Fantasy Craft game engine. It handles user authentication, game distribution (WASM), cloud telemetry, and provides a community platform for developers.

---

## ✨ Key Features

* **Modern Admin UI:** Powered by **[Django Unfold](https://github.com/unfoldadmin/django-unfold)**, offering a clean, Tailwind-based interface for management.
* **Robust Authentication:** Custom User model extending `AbstractUser` with:
    * 🌍 **Localization:** Timezone-aware (via `django-timezone-field`) and Country management (via `django-countries`).
    * 🖼️ **Avatar System:** Automatic fallback to username initials if no image is provided.
* **Full Internationalization (i18n):**
    * Bilingual support (English/French) via `django-modeltranslation`.
    * URL-based language prefixing (e.g., `/fr/admin/`).
    * Integrated translation UI with **Django Rosetta**.
* **Frontend Architecture:**
    * **Tailwind CSS** integrated via `django-tailwind` with Hot Module Replacement (HMR).
    * Responsive, dark-mode first design.
* **Developer Experience:**
    * Debug Toolbar configured for local development.

---

## 🛠️ Tech Stack

* **Backend:** Django 5.x, Python 3.12+
* **Frontend:** Tailwind CSS, PostCSS
* **Database:** MySQL (Dev), PostgreSQL (Prod - Ready)
* **Utilities:**
    * `django-modeltranslation` (DB Translation)
    * `django-rosetta` (Translation UI)

---

## 🚀 Getting Started

### Prerequisites

* **Python 3.10+**
* **Node.js & npm** (Required for Tailwind CSS compilation)

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/ikigami0513/foxvoid.git](https://github.com/ikigami0513/foxvoid.git)
    cd foxvoid
    ```

2.  **Install Python dependencies**
    ```bash
    poetry install
    ```

3.  **Activate the virtual environment**
    ```bash
    poetry shell
    ```

4.  **Install Node.js dependencies (Tailwind)**
    ```bash
    python manage.py tailwind install
    ```

5.  **Apply migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

### 🏃‍♂️ Running the Project

To run the project with hot-reloading for Tailwind, you need two terminal instances:

**Terminal 1: Django Server**
```bash
python manage.py runserver
```

**Terminal 2: Tailwind Watcher
```
python manage.py tailwind start
```

Visit http://127.0.0.1:8000/ to see the landing page, or http://127.0.0.1:8000/admin/ for the dashboard.

### 📂 Project Structure
```
foxvoid/
├── core/                 # Project configuration (settings, wsgi, urls)
├── authentication/       # Custom User model & Auth logic
├── public/               # Landing pages & Marketing views
├── theme/                # Tailwind CSS configuration & source files
├── locale/               # Translation files (.po/.mo)
├── static/               # Compiled static assets
└── templates/            # Global HTML templates
```

### 🌍 Internationalization

To update translations:

1.  **Generate message files (scans code & templates):**

```
python manage.py makemessages -l fr
```

2. **Translate using the admin interface at /rosetta/ or edit .po files manually.**

3. **Compile messages:**
```
python manage.py compilemessages
```

---

## 📄 Licensing: Foxvoid Platform is strictly licensed under the GNU AGPLv3.

This software is free to use for personal or educational purposes. Commercial Restriction: If you use this software to provide a SaaS (Software-as-a-Service) product that competes with Foxvoid Studio, you must release your entire source code under the AGPLv3.

For a commercial, non-copyleft license (to run a private fork without sharing code), please contact contact@foxvoid.com.

---

## 🤝 Related Projects
- [Fantasy Craft](https://github.com/ikigami0513/fantasy_craft)
