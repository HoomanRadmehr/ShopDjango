# Generated by Django 3.1.6 on 2021-02-22 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='availabe',
            new_name='available',
        ),
    ]