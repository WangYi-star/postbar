# Generated by Django 3.2 on 2021-07-01 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_usermodel_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
