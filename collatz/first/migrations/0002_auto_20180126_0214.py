# Generated by Django 2.0.1 on 2018-01-25 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='no',
        ),
        migrations.DeleteModel(
            name='Number',
        ),
    ]