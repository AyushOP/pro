# Generated by Django 3.1.2 on 2020-12-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0015_contact_email1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='institution',
            new_name='institute_name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='school',
            field=models.CharField(blank=True, choices=[('NA', 'NA'), ('School 1', 'School 1'), ('School 2', 'School 2'), ('School 3', 'School 3')], default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='stream',
            field=models.CharField(blank=True, choices=[('NA', 'NA'), ('Stream1.1', 'Stream1.1'), ('Stream 1.2', 'Stream 1.2'), ('Stream 1.3', 'Stream 1.3')], default='NA', max_length=20),
        ),
    ]
