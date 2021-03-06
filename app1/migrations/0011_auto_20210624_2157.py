# Generated by Django 3.2 on 2021-06-24 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20210623_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='postid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='recent',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.loginmodel'),
        ),
        migrations.AlterField(
            model_name='replymodel',
            name='delete',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='replymodel',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='replymodel',
            name='postid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.postmodel'),
        ),
        migrations.AlterField(
            model_name='replymodel',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.loginmodel'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.loginmodel'),
        ),
    ]
