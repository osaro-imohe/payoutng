# Generated by Django 2.1.2 on 2018-12-20 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0005_auto_20181211_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='condition',
        ),
    ]