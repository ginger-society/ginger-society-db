# Generated by Ginger 5.3.4 on 2024-09-08 09:02

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0029_organization_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="dbschema",
            name="db_type",
            field=models.CharField(
                choices=[
                    ("rdbms", "rdbms"),
                    ("cache", "cache"),
                    ("documentdb", "documentdb"),
                ],
                default="rdbms",
                max_length=50,
            ),
        ),
    ]
