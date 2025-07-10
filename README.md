# Django Multitenant SaaS Starter

A **Django + django‑tenants + Django REST Framework** starter template that shows how to build a schema‑based multi‑tenant Software‑as‑a‑Service (SaaS) platform.

Key highlights:

* Isolates every tenant in its own **PostgreSQL schema** 🔒
* **API‑first** architecture—easy to plug in web, mobile or third‑party apps
* Automatically creates a new schema and runs migrations whenever a tenant is created
* Sample **`notes`** app that demonstrates CRUD and slug‑based routing
* **Pytest** test‑suite covering models, serializers and API endpoints

> **Live Demo Idea**   Point `acme.localhost:8000` and `public.localhost:8000` to the same server, then visit `/notes/` to see tenant isolation in action.

---

## Table of Contents

* [Quick Start](#quick-start)
* [Project Structure](#project-structure)
* [Running Tests](#running-tests)
* [Common Management Commands](#common-management-commands)
---

## Quick Start

```bash
# 1 Clone the repo
$ git clone https://github.com/YOURNAME/django-multitenant-saas.git
$ cd django-multitenant-saas

# 2 Create & activate virtualenv
$ python -m venv .venv
# MacOS
$ source .venv/bin/activate   
# Windows: 
$ .venv\Scripts\activate

# 3 Install dependencies
$ pip install -r requirements.txt

# 4 Copy env vars template & fill in DB, SECRET_KEY …
$ cp .env.example .env

# 5 Run shared migrations and create a super‑user
$ python manage.py migrate_schemas --shared
$ python manage.py createsuperuser --schema public

# 6 Start the dev server
$ python manage.py runserver
```

---

## Project Structure

```
django_multitenant_saas/
│
├─ clients/                # Tenant & Domain models
│   ├─ tests/
│   └─ migrations/
├─ notes/                  # Sample app (API + tests)
│   ├─ tests/
│   └─ migrations/
│
├─ django_multitenant_saas/  # Project settings
├─ pytest.ini
├─ .env.example
├─ .envrc
├─ requirements.txt
└─ README.md
```

---

## Running Tests

```bash
pytest -q
```

The `pytest‑django` plugin builds a disposable test database and spins up a tenant schema for each test class.

---

## Common Management Commands

| Purpose                       | Command                                                           |
| ----------------------------- | ----------------------------------------------------------------- |
| Create a new tenant           | `python manage.py create_tenant --schema acme --name "Acme Inc."` |
| Run migrations for one tenant | `python manage.py migrate_schemas --tenant acme`                  |
| Load sample data              | `python manage.py loaddata fixtures/sample.json`                  |

---