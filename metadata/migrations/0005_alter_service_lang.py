# Generated by Ginger 5.3.4 on 2024-07-24 06:35

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0004_alter_service_envs_spec"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="lang",
            field=models.CharField(
                blank=True,
                choices=[
                    ("typescript_fetch", "typescript-fetch"),
                    ("rust", "Rust"),
                    ("python", "Python"),
                ],
                max_length=25,
                null=True,
            ),
        ),
    ]
