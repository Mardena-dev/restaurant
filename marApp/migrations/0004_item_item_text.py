# Generated by Django 5.0.1 on 2024-01-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marApp', '0003_alter_staff_staff_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_text',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
