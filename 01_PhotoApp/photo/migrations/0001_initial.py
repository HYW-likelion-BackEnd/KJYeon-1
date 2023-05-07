# Generated by Django 4.2.1 on 2023-05-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
