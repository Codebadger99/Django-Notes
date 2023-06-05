# Generated by Django 4.2.1 on 2023-06-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('Heading', models.TextField(blank=True, max_length=20)),
                ('title', models.TextField(max_length=250)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
