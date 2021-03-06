# Generated by Django 2.1 on 2018-08-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bbncreative_cms', '0015_auto_20180731_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageasset',
            name='aspect_ratio',
            field=models.CharField(
                choices=[('SQ', 'Square'), ('W1', '4:3 wide'), ('W2', '3:2 wide'), ('W3', '16:9 wide'),
                         ('T1', '3:4 tall'), ('T2', '2:3 tall'), ('T3', '9:16 tall')], default='W1', max_length=2),
        ),
    ]
