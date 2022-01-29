# Generated by Django 4.0.1 on 2022-01-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipPreferenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_profile_id', models.IntegerField()),
                ('available', models.BooleanField()),
                ('end_data', models.CharField(max_length=50)),
                ('university', models.BooleanField()),
                ('start_data', models.CharField(max_length=50)),
                ('student_preferred', models.IntegerField()),
            ],
        ),
    ]
