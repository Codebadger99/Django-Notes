# Generated by Django 4.2.1 on 2023-06-01 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notesinfo',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='notesinfo',
            name='Time',
        ),
    ]
