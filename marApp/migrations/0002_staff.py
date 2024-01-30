# Generated by Django 5.0.1 on 2024-01-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(blank=True, max_length=15, null=True)),
                ('staff_surname', models.CharField(blank=True, max_length=15, null=True)),
                ('staff_position', models.CharField(blank=True, max_length=20, null=True)),
                ('staff_email', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]