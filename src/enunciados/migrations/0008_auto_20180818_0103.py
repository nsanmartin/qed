# Generated by Django 2.1 on 2018-08-18 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enunciados', '0007_auto_20180818_0050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materia',
            options={'ordering': ['nombre']},
        ),
    ]
