# Generated by Django 4.1.7 on 2023-03-29 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PersonalManagement', '0003_doctordepartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('url', models.TextField()),
                ('image_type', models.CharField(choices=[('DoctorNotarizedImage', 1)], max_length=60)),
                ('base_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Image',
            },
        ),
    ]
