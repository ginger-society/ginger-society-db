# Generated by Ginger 5.3.13 on 2024-10-25 06:26

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0010_alter_app_group_alter_token_app"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="allow_registration",
            field=models.BooleanField(default=False),
        ),
    ]