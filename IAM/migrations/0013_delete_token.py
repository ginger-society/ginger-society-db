# Generated by GingerDJ 6.0.8 on 2024-12-12 04:43

from gingerdj.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0012_user_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='token',
        ),
    ]