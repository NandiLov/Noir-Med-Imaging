# Generated by Django 5.0 on 2023-12-21 11:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor_dashboard", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicalfile",
            name="file",
            field=models.FileField(
                default="medical_report.txt", upload_to="medical_files/"
            ),
        ),
        migrations.AlterField(
            model_name="medicalfile",
            name="uploaded_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="doctor_dashboard_reports",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="DicomImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="dicom_images/")),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctor_dashboard.patient",
                    ),
                ),
            ],
        ),
    ]
