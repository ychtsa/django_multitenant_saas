# clients/tests/conftest.py
import pytest
from django.test import Client as DjangoClient
from clients.models import Client as Tenant


@pytest.fixture
def django_client():
    return DjangoClient()


@pytest.fixture
def tenant(db):
    return Tenant.objects.create(name="Acme Co", schema_name="acme")
