# Generated by Django 5.1.2 on 2024-10-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singupc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('psw', models.CharField(max_length=122)),
                ('psw_repeat', models.CharField(max_length=122)),
                ('opp', models.CharField(max_length=122)),
            ],
        ),
    ]
