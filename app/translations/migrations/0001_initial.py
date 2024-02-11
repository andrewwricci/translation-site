# Generated by Django 4.2.9 on 2024-01-04 17:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Translated_Text',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('translated_text', models.CharField(max_length=10000)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translations.user')),
            ],
        ),
        migrations.CreateModel(
            name='Original_Text',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original_text', models.CharField(max_length=10000)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translations.user')),
            ],
        ),
    ]
