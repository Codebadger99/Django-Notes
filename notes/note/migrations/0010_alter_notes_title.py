# Generated by Django 4.2.1 on 2023-06-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_alter_notes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
