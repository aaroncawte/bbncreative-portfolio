# Generated by Django 2.1 on 2018-08-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bbncreative_cms', '0021_auto_20180822_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
