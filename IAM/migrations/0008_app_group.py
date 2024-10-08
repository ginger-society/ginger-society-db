# Generated by Ginger 5.3.13 on 2024-10-08 09:33

import ginger.db.models.deletion
from ginger.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("src", "0007_alter_api_token_token_str"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=ginger.db.models.deletion.SET_NULL,
                related_name="apps",
                to="src.group",
            ),
        ),
    ]
