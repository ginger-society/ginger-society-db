# Generated by Ginger 5.3.4 on 2024-09-12 05:41

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0033_alter_service_group_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
