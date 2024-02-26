# Generated by Django 4.1.7 on 2023-04-22 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0023_doctor_is_receive'),
        ('MedicalRecordManagement', '0007_prescription_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecord',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='User.doctor'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='User.patient'),
        ),
    ]
