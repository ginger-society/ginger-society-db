# Generated by Ginger 5.3.4 on 2024-09-18 12:20

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0034_organization_is_public"),
    ]

    operations = [
        migrations.AddField(
            model_name="dbschema",
            name="quick_links",
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="package",
            name="quick_links",
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name="service",
            name="quick_links",
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
