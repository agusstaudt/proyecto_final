# Generated by Django 4.2 on 2023-10-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppBlog", "0002_interesado_cuit_interesado_organizacion_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consultoria",
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
                ("servicio", models.CharField(max_length=40)),
            ],
        ),
    ]
