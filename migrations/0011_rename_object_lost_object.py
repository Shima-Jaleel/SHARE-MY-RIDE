# Generated by Django 3.2.19 on 2024-04-09 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_feedback_lost_object'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lost',
            old_name='object',
            new_name='Object',
        ),
    ]
