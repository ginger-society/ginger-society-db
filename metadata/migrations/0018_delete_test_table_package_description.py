# Generated by Ginger 5.3.4 on 2024-08-13 05:37

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0017_remove_package_description"),
    ]

    operations = [
        migrations.DeleteModel(
            name="test_table",
        ),
        migrations.AddField(
            model_name="package",
            name="description",
            field=models.CharField(blank=True, max_length=25000, null=True),
        ),
    ]
