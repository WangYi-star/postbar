# Generated by Django 3.2 on 2021-06-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_usermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='uid',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
