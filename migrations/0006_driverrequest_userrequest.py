# Generated by Django 3.2.19 on 2024-03-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_book_availableseats'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('request', models.CharField(max_length=100)),
                ('replay', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('DRIVER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.driver')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='DriverRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('request', models.CharField(max_length=100)),
                ('replay', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('DRIVER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.driver')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]