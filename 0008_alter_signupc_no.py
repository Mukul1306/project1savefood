# Generated by Django 5.1.2 on 2024-10-26 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0007_alter_signupc_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupc',
            name='No',
            field=models.IntegerField(max_length=8),
        ),
    ]
