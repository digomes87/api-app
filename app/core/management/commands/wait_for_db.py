from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django Command to wait for database"""

    def handle(self, *args, **options):
        pass