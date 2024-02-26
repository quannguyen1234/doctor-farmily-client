# Generated by Django 4.1.7 on 2023-05-22 14:59

import apps.Transaction.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaction', '0025_alter_wallet_base_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(default=datetime.date.today, validators=[apps.Transaction.models.validate_month_year]),
        ),
    ]
