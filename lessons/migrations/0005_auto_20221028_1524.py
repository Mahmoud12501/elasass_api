# Generated by Django 3.2 on 2022-10-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20221025_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Class_name'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Subject_name '),
        ),
    ]