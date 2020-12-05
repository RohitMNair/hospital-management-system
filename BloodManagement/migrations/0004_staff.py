# Generated by Django 3.1.4 on 2020-12-05 04:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloodManagement', '0003_remove_patient_blood_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('address', models.TextField()),
                ('job', models.CharField(choices=[('IT', 'IT'), ('Elec', 'Electrician'), ('Nurse', 'Nurse')], max_length=5)),
            ],
        ),
    ]
