# Generated by Ginger 5.3.4 on 2024-07-21 19:11

from gingerdj.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("src", "0002_test_table"),
    ]

    operations = [
        migrations.DeleteModel(
            name="test_table",
        ),
    ]
