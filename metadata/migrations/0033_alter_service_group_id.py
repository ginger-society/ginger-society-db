# Generated by Ginger 5.3.4 on 2024-09-10 06:06

from ginger.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0032_service_cache_schema_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='group_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]