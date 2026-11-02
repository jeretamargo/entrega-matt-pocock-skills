from django.db import migrations, models
import django.db.models.deletion


def copy_existing_cancellations(apps, schema_editor):
    Registration = apps.get_model("activities", "Registration")
    RegistrationCancellation = apps.get_model("activities", "RegistrationCancellation")
    RegistrationCancellation.objects.using(schema_editor.connection.alias).bulk_create(
        RegistrationCancellation(registration_id=registration.pk, cancelled_at=registration.cancelled_at)
        for registration in Registration.objects.using(schema_editor.connection.alias).exclude(cancelled_at__isnull=True)
    )


class Migration(migrations.Migration):
    dependencies = [("activities", "0003_activity_responsible")]

    operations = [
        migrations.CreateModel(
            name="RegistrationCancellation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cancelled_at", models.DateTimeField(verbose_name="cancelación")),
                ("registration", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="cancellations", to="activities.registration")),
            ],
            options={"ordering": ["-cancelled_at", "-pk"], "verbose_name": "cancelación de inscripción"},
        ),
        migrations.RunPython(copy_existing_cancellations, migrations.RunPython.noop),
    ]
