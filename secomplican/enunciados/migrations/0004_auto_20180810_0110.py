# Generated by Django 2.1 on 2018-08-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0003_auto_20180808_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practica',
            name='titulo',
            field=models.CharField(blank=True, default='', max_length=1023),
        ),
    ]
