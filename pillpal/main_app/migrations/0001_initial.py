# Generated by Django 2.2.12 on 2020-09-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_issue_date', models.DateField()),
                ('prescription_filled_date', models.DateField()),
                ('instructions', models.CharField(max_length=250)),
                ('delivery', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=100)),
                ('refills', models.IntegerField()),
            ],
        ),
    ]
