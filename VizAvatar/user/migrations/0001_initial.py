# Generated by Django 5.0.6 on 2024-06-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("height", models.DecimalField(decimal_places=2, max_digits=5)),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "users",
            },
        ),
    ]