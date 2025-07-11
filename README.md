# Django Multitenant SaaS Starter

A **Django + django‑tenants + Django REST Framework** starter template that shows how to build a schema‑based multi‑tenant Software‑as‑a‑Service (SaaS) platform.

Key highlights:

* Isolates every tenant in its own **PostgreSQL schema** 🔒
* **API‑first** architecture—easy to plug in web, mobile or third‑party apps
* Automatically creates a new schema and runs migrations whenever a tenant is created
* Sample **`notes`** app that demonstrates CRUD and slug‑based routing
* **Pytest** test‑suite covering models, serializers and API endpoints

> **Live Demo Idea**   Point `acme.localhost:8000` and `perfect.localhost:8000` to the same server, then visit `/notes/` to see tenant isolation in action.

---

## Table of Contents

* [Create Database & User](#create-database-user)
* [Quick Start](#quick-start)
* [Create Tenants & Admin Users](#create-tenants-admin-users)
* [Project Structure](#project-structure)
* [Running Tests](#running-tests)
* [Common Management Commands](#common-management-commands)

---

## Create Database & User

```bash
# Create a user
$ createuser --interactive --pwprompt <YOUR_USER_NAME>

# Create a database
$ createdb -O <YOUR_USER_NAME> <YOUR_DATABASE_NAME>

# Grant User permission to create schema
$ psql -d <YOUR_DATABASE_NAME> -c "GRANT CREATE ON DATABASE <YOUR_DATABASE_NAME> TO <YOUR_USER_NAME>"

```

---

## Quick Start

```bash
# Prerequisites
Check first:
    python --version # ≥ 3.10
    psql --version   # ≥ 13
    git --version

# 1 Clone & enter repo
$ git clone https://github.com/YOURNAME/django-multitenant-saas.git
$ cd django-multitenant-saas

# 2 Create & activate virtualenv
$ python -m venv .venv
# MacOS
$ source .venv/bin/activate   
# Windows: 
$ .venv\Scripts\activate

# 3 Install dependencies
$ pip install --upgrade pip
$ pip install -r requirements.txt

# 4 Create the environment file (.env)
$ cp .env.example .env  # Windows: copy .env.example .env

# 5 Get the secret key
$ python manage.py shell
>>>from django.core.management.utils import get_random_secret_key
>>>print(get_random_secret_key())

Open .env and fill in:
    # Use get_random_secret_key to generate
    SECRET_KEY=<YOUR_DJANGO_SECRET_KEY>      
    DATABASE_URL=postgres://<YOUR_USER_NAME>:<YOUR_PASSWORD>@localhost:5432/<YOUR_DATABASE_NAME>
    DEBUG=True
    ALLOWED_HOSTS=.localhost,127.0.0.1,localhost


# 6 Run migrations
$ python manage.py makemigrations  # create a migration file
$ python manage.py migrate_schemas --shared  # for public
$ python manage.py migrate_schemas --tenant  # for all of tenants
$ python manage.py migrate_schemas --schema=<YOUR_SCHEMA_NAME>  # for the specific tenant

# 7 Start the dev server
$ python manage.py runserver

# 8 Browse and Check
Admin -> http://127.0.0.1:8000/admin/
API   -> http://<YOUR_DOMAIN>:8000/notes/    # e.g. http://perfect.localhost:8000/notes

```

---

## Create Tenants & Admin Users

```bash
# Create a new tenant with the built-in management command 
$ python manage.py create_tenant
Enter the information: <schema name>, <name>, <paid until>, <on trial>
After auto migration, enter the information: <domain>, <is primary>

# Create New Tenant with Django Shell
$ python manage.py shell
>>>from clients.models import Client, Domain
>>>from datetime import date
>>>client = Client(schema_name="<YOUR_SCHEMA_NAME>", name="<YOUR_NAME>", paid_until=date(<YOUR_DATE>), on_trial=<TRUE_OR_FALSE>)
>>>client.save
>>>Domain.objects.create(domain="<YOUR_DOMAIN_NAME>", tenant=client, is_primary=True)

# Create a superuser
$ python manage.py createsuperuser  # public's superuser
$ python manage.py createsuperuser --schema=<YOUR_SCHEMA_NAME> # tenant's superuser

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
├─ .gitignore
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