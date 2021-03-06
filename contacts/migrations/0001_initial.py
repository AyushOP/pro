# Generated by Django 3.1.2 on 2020-11-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_name', models.CharField(choices=[('n', 'NA'), ('t', 'TCS'), ('i', 'INFOSYS'), ('a', 'ACCENTURE'), ('a', 'AMAZON'), ('h', 'HIGHRADIUS')], default='NA', max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('salutation', models.CharField(choices=[('n', 'NA'), ('c', 'Colonel'), ('mr', 'Mr.'), ('mrs', 'Mrs.'), ('D', 'Dr')], default='NA', max_length=20)),
                ('referred_by', models.CharField(choices=[('n', 'NA'), ('a', 'Mr A.'), ('b', 'Mr B'), ('c', 'Mr C')], default='NA', max_length=20)),
                ('designation', models.CharField(choices=[('n', 'NA'), ('h', 'HR'), ('f', 'Finance'), ('a', 'Administration'), ('a', 'Accounts'), ('i', 'IT'), ('m', 'Management'), ('ma', 'Marketing'), ('t', 'Technical'), ('p', 'Purchase')], default='NA', max_length=20)),
                ('department', models.CharField(choices=[('n', 'NA'), ('h', 'HR'), ('f', 'Finance'), ('ad', 'Administration'), ('ac', 'Accounts'), ('i', 'IT'), ('m', 'Management'), ('ma', 'Marketing'), ('t', 'Technical'), ('p', 'Purchase')], default='NA', max_length=20)),
                ('email', models.EmailField(max_length=70)),
                ('mob_no', models.CharField(max_length=20)),
                ('direct_no', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('school', models.CharField(choices=[('n', 'NA'), ('s1', 'STREAM_1'), ('s2', 'STREAM_2'), ('s3', 'STREAM_3')], default='NA', max_length=20)),
                ('y_of_p', models.CharField(max_length=10)),
                ('degree', models.CharField(max_length=50)),
                ('month', models.CharField(choices=[('n', 'NA'), ('j1', 'JANUARY'), ('j2', 'FEBRUARY')], default='NA', max_length=20)),
                ('year', models.CharField(choices=[('n', 'NA'), ('j1', '2001'), ('j2', '2002')], default='NA', max_length=20)),
                ('Linkedin', models.CharField(max_length=30)),
                ('Facebook', models.CharField(max_length=30)),
                ('Twitter', models.CharField(max_length=30)),
                ('Of_details', models.CharField(choices=[('n', 'NA'), ('hd', 'Head office'), ('f', 'Factory plant'), ('bch', 'Branch office'), ('p', 'Project_site'), ('r', 'Regional_office'), ('re', 'Registered_office'), ('z', 'Zonal_office')], default='NA', max_length=20)),
                ('Board_line_number', models.CharField(max_length=20)),
                ('Address', models.TextField(max_length=200)),
                ('Country', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=15)),
            ],
        ),
    ]
