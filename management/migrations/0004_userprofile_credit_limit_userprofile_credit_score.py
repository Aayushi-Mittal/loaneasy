# Generated by Django 4.0.3 on 2022-03-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_loan_application_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='credit_limit',
            field=models.CharField(default=100000, max_length=15),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='credit_score',
            field=models.CharField(default=20, max_length=3),
        ),
    ]
