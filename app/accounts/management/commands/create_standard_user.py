import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Creates a standard user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--email', help="User's email")
        parser.add_argument('--phone-number', help="User's phone number")
        parser.add_argument('--password', help="User's password")

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.filter(email=options['email']).exists():
            print(f"User account {options['email']} already exists, skipping...")
        else:
            print(f"Creating user account {options['email']}...")
            User.objects.create_user(email=options['email'],
                                     phone_number=options['phone_number'],
                                     password=options['password'])
            if User.objects.filter(email=options['email']).exists():
                print("Account creation succeeded!")
