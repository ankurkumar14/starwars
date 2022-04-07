from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FavouriteMovies",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=100)),
                ("movie", models.CharField(max_length=100)),
                ("release", models.CharField(max_length=100)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="FavouritePlanets",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=100)),
                ("planet", models.CharField(max_length=100)),
                ("population", models.CharField(max_length=100)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="SavedPlanets",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=100)),
                ("planet", models.CharField(max_length=100)),
                ("population", models.CharField(max_length=100)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
