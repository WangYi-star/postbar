# Generated by Django 3.2 on 2021-06-22 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_postmodel_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='content',
        ),
    ]
