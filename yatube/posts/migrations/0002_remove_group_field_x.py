# Generated by Django 2.2.19 on 2021-10-24 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='field_X',
        ),
    ]