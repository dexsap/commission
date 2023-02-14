# Generated by Django 4.0.4 on 2023-02-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeProdDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(max_length=50)),
            ],
        ),
    ]
