# Generated by Django 5.0.3 on 2024-05-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('path', models.CharField(default='', max_length=255)),
                ('extension', models.CharField(default='', max_length=10)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]