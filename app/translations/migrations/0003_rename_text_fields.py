# Generated by Django 4.2.9 on 2024-01-05 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0002_add_last_updated_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='original_text',
            old_name='original_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='translated_text',
            old_name='translated_text',
            new_name='text',
        ),
    ]
