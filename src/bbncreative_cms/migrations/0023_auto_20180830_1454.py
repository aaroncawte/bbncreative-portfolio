# Generated by Django 2.1 on 2018-08-30 13:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bbncreative_cms', '0022_feed_date_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feed',
            options={'ordering': ['-date_updated']},
        ),
    ]
