# Generated by Django 5.2.2 on 2025-06-10 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
