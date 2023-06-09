# Generated by Django 4.2 on 2023-04-12 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Platform",
            fields=[
                (
                    "name",
                    models.TextField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.TextField(max_length=200)),
                ("studio", models.TextField(max_length=100)),
                ("release_date", models.DateField()),
                ("ratings", models.IntegerField(null=True)),
                (
                    "platforms",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="games.platform"
                    ),
                ),
            ],
        ),
    ]
