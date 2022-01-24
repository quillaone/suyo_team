# Generated by Django 4.0.1 on 2022-01-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]