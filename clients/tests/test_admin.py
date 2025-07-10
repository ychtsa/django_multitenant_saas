import pytest
from django.contrib import admin
from clients.models import Client, Domain

pytestmark = pytest.mark.django_db


def test_client_model_registered():
    assert Client in admin.site._registry
    assert "name" in admin.site._registry[Client].list_display


def test_domain_model_registered():
    assert Domain in admin.site._registry
    assert "domain" in admin.site._registry[Domain].list_display
