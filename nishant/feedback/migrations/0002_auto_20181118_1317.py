# Generated by Django 2.1.2 on 2018-11-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
