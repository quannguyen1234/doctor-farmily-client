# Generated by Django 4.1.7 on 2023-05-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction', '0007_transaction_base_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticbilldetail',
            name='distance',
            field=models.FloatField(default=0),
        ),
    ]
