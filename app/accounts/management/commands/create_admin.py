import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--email', help="Admin's email")
        parser.add_argument('--password', help="Admin's password")

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.filter(email=options['email']).exists():
            print(f"Admin account {options['email']} already exists, skipping...")
        else:
            print(f"Creating admin account {options['email']}...")
            User.objects.create_superuser(email=options['email'],
                                          password=options['password'])
            if User.objects.filter(email=options['email']).exists():
                print("Account creation succeeded!")
