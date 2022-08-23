# Generated by Django 4.1 on 2022-08-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
