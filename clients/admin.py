from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Client, Domain


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    """
    Admin interface for Client:
    - TenantAdminMixin: displays schema switcher in the admin UI
    - Inline editing of Domain entries on the Client page
    """
    list_display = ("name", "schema_name", "paid_until", "on_trial")
    search_fields = ("name", "schema_name")
    list_filter = ("on_trial",)
    ordering = ("-paid_until",)

    class DomainInline(admin.TabularInline):
        model = Domain
        extra = 1

    inlines = [DomainInline]


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    """
    Admin interface for Domain:
    Displays the domain name and the associated tenant.
    """
    list_display = ("domain", "tenant", "is_primary")
    search_fields = ("domain",)
    list_filter = ("is_primary",)
    raw_id_fields = ("tenant",)