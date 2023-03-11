# Generated by Django 4.1.7 on 2023-03-06 11:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
        ("accounts", "0003_userprofile_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="OtpRecord",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("phone", models.CharField(max_length=16)),
                ("otp", models.PositiveIntegerField()),
                ("attempts", models.PositiveIntegerField(default=1)),
                ("is_applied", models.BooleanField(default=False)),
                ("date_added", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "date_updated",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "country",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.country",
                    ),
                ),
            ],
            options={
                "verbose_name": "Otp Record",
                "verbose_name_plural": "Otp Records",
                "db_table": "accounts_otp_record",
                "ordering": ("-date_added",),
            },
        ),
    ]