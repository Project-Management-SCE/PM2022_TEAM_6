# Generated by Django 4.0.3 on 2022-04-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_messegerequest_id_alter_school_id'),
        ('voulnteers', '0006_alter_volnteer_first_name_alter_volnteer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='volnteer',
            name='publications',
            field=models.ManyToManyField(to='manager.school'),
        ),
    ]
