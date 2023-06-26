# Generated by Django 4.1.7 on 2023-06-21 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0024_absence_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="absence",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_absences",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="absence",
            name="beneficiary",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="approved_absences",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
