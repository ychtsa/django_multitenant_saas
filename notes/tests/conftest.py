import pytest
from rest_framework.test import APIClient
from django_tenants.utils import schema_context
from clients.models import Client, Domain

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture(scope="session")
def tenant(django_db_blocker):
    with django_db_blocker.unblock():
        tenant, _ = Client.objects.get_or_create(
            schema_name="test",
            defaults={"name": "Test Tenant", "paid_until": "2099-12-31"},
        )
        tenant.create_schema(check_if_exists=True, sync_schema=True)

        Domain.objects.get_or_create(domain="testserver", tenant=tenant, is_primary=True)
        return tenant

@pytest.fixture(autouse=True)
def _activate_tenant_schema(tenant):
    with schema_context(tenant.schema_name):
        yield
