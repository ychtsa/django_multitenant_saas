import pytest
from clients.models import Client, Domain

pytestmark = pytest.mark.django_db


class TestClientModel:
    def test_create_client(self):
        client = Client.objects.create(name="Acme Co", schema_name="acme")
        assert client.pk is not None
        assert client.name == "Acme Co"
        assert client.schema_name == "acme"

    def test_create_domain(self, tenant):
        domain = Domain.objects.create(domain="beta.example.com", tenant=tenant)
        assert domain.pk is not None
        assert domain.domain == "beta.example.com"
        assert domain.tenant == tenant
