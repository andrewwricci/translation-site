# Generated by Django 4.2.9 on 2024-02-22 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0003_alter_originaltext_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translatedtext',
            old_name='original_text_id',
            new_name='originaltext_id',
        ),
    ]
