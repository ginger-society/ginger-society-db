# Generated by GingerDJ 6.0.8 on 2024-12-10 12:30

from gingerdj.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0011_app_allow_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
