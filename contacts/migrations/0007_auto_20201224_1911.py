# Generated by Django 3.1.2 on 2020-12-24 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20201224_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='y_of_p',
            new_name='yop',
        ),
    ]