# Generated by Django 3.0.5 on 2020-04-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='date_time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='teacher_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
