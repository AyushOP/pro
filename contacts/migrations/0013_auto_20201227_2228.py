# Generated by Django 3.1.2 on 2020-12-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20201225_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='department',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]