# Generated by Django 4.1.7 on 2023-05-21 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Transaction', '0011_report_revenue'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactiom_to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='base_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactiom_from_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
