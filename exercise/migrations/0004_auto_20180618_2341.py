# Generated by Django 2.0 on 2018-06-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_auto_20180618_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='summary',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
