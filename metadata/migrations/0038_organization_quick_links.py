# Generated by Ginger 5.3.4 on 2024-10-03 06:50

from ginger.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0037_service_message_queue_schema_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='quick_links',
            field=models.TextField(max_length=20000, null=True),
        ),
    ]
