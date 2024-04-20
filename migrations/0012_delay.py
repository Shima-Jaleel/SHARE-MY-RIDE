# Generated by Django 3.2.19 on 2024-04-11 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_object_lost_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notification', models.CharField(max_length=100)),
                ('replay', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('DRIVER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.driver')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]