# Generated by Django 5.1.1 on 2024-09-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
