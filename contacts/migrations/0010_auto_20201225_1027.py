# Generated by Django 3.1.2 on 2020-12-25 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_contact_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='co_name',
            field=models.CharField(choices=[('NA', 'n'), ('TCS', 'TCS'), ('INFOSYS', 'INFOSYS'), ('ACCENTURE', 'ACCENTURE'), ('AMZON', 'AMAZON'), ('HIGHRADIUS', 'HIGHRADIUS')], default='NA', max_length=20),
        ),
    ]
