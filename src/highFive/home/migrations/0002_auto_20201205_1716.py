# Generated by Django 3.2 on 2020-12-06 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pickUpTime',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='item_id',
            field=models.IntegerField(default=85997),
        ),
    ]
