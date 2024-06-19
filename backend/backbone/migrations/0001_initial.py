# Generated by Django 5.0.6 on 2024-06-19 19:18

import backbone.manager
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consent",
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
                (
                    "consent_type",
                    models.CharField(
                        choices=[
                            ("INFORMATION", "Information"),
                            ("BIOMETRIC", "Biometric"),
                        ],
                        default="INFORMATION",
                        max_length=16,
                    ),
                ),
                ("change_date", models.DateTimeField(auto_now=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Log",
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
                (
                    "log_type",
                    models.CharField(
                        choices=[
                            ("LOGIN", "Login"),
                            ("CREATE", "Create"),
                            ("DELETE", "Delete"),
                            ("IMPORT", "Import"),
                            ("ADD_PARENT", "Add Parent"),
                            ("HISTORY", "History"),
                            ("ADD_PERMISSION", "Add Permission"),
                            ("SIGN", "Sign"),
                            ("WARNING", "Warning"),
                            ("ERROR", "Error"),
                            ("INFO", "Info"),
                        ],
                        default="LOGIN",
                        max_length=16,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("data", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="UserConsent",
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
                ("signing_date", models.DateTimeField(auto_now_add=True)),
                ("seen_changes", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150)),
                ("last_name", models.CharField(blank=True, max_length=150)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, default="", max_length=16),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "teacher_perm",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "None"), (1, "Partial"), (2, "Full")], default=0
                    ),
                ),
                (
                    "parent_perm",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "None"), (1, "Partial"), (2, "Full")], default=0
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", backbone.manager.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name="consent",
            constraint=models.UniqueConstraint(
                fields=("consent_type", "description"),
                name="unique_consent_type_description",
            ),
        ),
        migrations.AddField(
            model_name="userconsent",
            name="consent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="backbone.consent"
            ),
        ),
        migrations.AddField(
            model_name="userconsent",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddConstraint(
            model_name="userconsent",
            constraint=models.UniqueConstraint(
                fields=("user", "consent"), name="unique_user_consent"
            ),
        ),
    ]
