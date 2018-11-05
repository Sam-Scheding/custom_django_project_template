from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.core.management.utils import get_random_secret_key

class Command(BaseCommand):

    help = 'Generate a valid secret key for Django'

    def handle(self, *args, **options):

        key = get_random_secret_key()
        print('SECRET_KEY = "{}"'.format(key))
