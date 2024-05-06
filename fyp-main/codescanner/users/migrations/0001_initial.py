# Generated by Django 5.0.3 on 2024-05-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('path', models.CharField(default='', max_length=255)),
                ('extension', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
