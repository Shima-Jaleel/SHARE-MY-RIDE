# Generated by Django 3.2.19 on 2024-03-27 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_book_availableseats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='AVAILABLESEATS',
        ),
    ]
