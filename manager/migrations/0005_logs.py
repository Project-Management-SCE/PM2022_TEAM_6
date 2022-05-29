# Generated by Django 3.2.13 on 2022-05-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_volinstances'),
    ]

    operations = [
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=400)),
                ('done_by', models.IntegerField()),
                ('done_to', models.IntegerField()),
                ('activity_date', models.DateTimeField()),
            ],
        ),
    ]