from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.core.management import call_command
from django.db import transaction
# Create your models here.

class Client(TenantMixin):
    """
    Tenant model representing a customer in the SaaS system.
    TenantMixin adds fields like schema_name and controls schema creation.
    """
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)

    # Automatically create a new schema when a Client is created
    auto_create_schema = True
    def save(self, *args, **kwargs):
        # Check if this is a new instance
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            # Run migrations for the new tenant schema after committing
            transaction.on_commit(
                lambda: call_command(
                    "migrate_schemas", tenant=[self.schema_name], interactive=False, verbosity=0
                )
            )

class Domain(DomainMixin):
    """
    Domain model linking a domain name to a Client (tenant).
    DomainMixin sets up the foreign key to Client.
    """
    pass