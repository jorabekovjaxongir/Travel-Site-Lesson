# Generated by Django 5.1.6 on 2025-02-15 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='category',
        ),
    ]
