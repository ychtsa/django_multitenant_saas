import sys
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from clients.models import Client, Domain

class Command(BaseCommand):
    help = 'Create the public schema tenant and its domain entries'

    def add_arguments(self, parser):
        parser.add_argument(
            '--schema-name',
            default='public',
            help='The schema name for the public tenant (default: public)'
        )
        parser.add_argument(
            '--domains',
            nargs='+',
            default=['localhost', '127.0.0.1'],
            help='One or more domains for the public tenant (default: localhost 127.0.0.1)'
        )
        parser.add_argument(
            '--name',
            default='Public Tenant',
            help='Display name for the public tenant'
        )

    def handle(self, *args, **options):
        schema_name = options['schema_name']
        domains = options['domains']
        display_name = options['name']

        if Client.objects.filter(schema_name=schema_name).exists():
            self.stdout.write(self.style.WARNING(
                f"Tenant with schema '{schema_name}' already exists."
            ))
            return

        try:
            with transaction.atomic():
                # Create the public tenant
                public = Client(
                    schema_name=schema_name,
                    name=display_name,
                    paid_until=None,
                    on_trial=False
                )
                public.auto_create_schema = False
                public.save()

                # Create one Domain entry per given domain
                for domain in domains:
                    Domain.objects.create(
                        domain=domain,
                        tenant=public,
                        is_primary=(domain == domains[0])
                    )

                self.stdout.write(self.style.SUCCESS(
                    f"Public tenant '{schema_name}' and domains '{' '.join(domains)}' created successfully."
                ))

        except Exception as e:
            raise CommandError(f"Error creating public tenant: {e}")
