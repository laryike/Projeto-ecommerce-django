# Generated by Django 3.0.8 on 2020-07-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200724_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='complet',
            new_name='complete',
        ),
    ]
