# Generated by Ginger 5.3.4 on 2024-08-20 07:07

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0025_dbschema_branch_pipeline_status_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="organization",
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
                ("slug", models.CharField(max_length=100)),
                ("group_id", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "organization",
            },
        ),
        migrations.AddField(
            model_name="dbschema",
            name="repo_origin",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="package",
            name="repo_origin",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="service",
            name="repo_origin",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
