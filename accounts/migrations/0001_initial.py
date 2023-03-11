# Generated by Django 4.1.7 on 2023-03-06 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("auto_id", models.PositiveIntegerField(db_index=True, unique=True)),
                ("date_added", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("date_updated", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("username", models.CharField(blank=True, max_length=128, null=True)),
                ("password", models.TextField(blank=True, null=True)),
                ("date_of_birth", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(blank=True, max_length=128, null=True)),
                ("phone", models.CharField(blank=True, max_length=128, null=True)),
                ("is_verified", models.BooleanField(default=False)),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.country",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator_%(class)s_objects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updater",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="updator_%(class)s_objects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "user profile",
                "verbose_name_plural": "user profiles",
                "db_table": "accounts__profile",
                "ordering": ("name",),
            },
        ),
    ]