# Generated by Django 4.0.3 on 2022-04-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='coord_id',
            field=models.IntegerField(),
        ),
    ]
