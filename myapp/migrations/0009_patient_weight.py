# Generated by Django 5.0.4 on 2024-09-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_patient_age_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
