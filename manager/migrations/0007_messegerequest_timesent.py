# Generated by Django 4.0.3 on 2022-04-15 21:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_schoolrequest_volnteer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='messegerequest',
            name='timesent',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
