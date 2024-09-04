# Generated by Ginger 5.3.4 on 2024-08-25 14:36

import ginger.db.models.deletion
from ginger.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_rename_app_url_app_app_url_dev_app_app_url_prod_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='api_token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=ginger.db.models.deletion.CASCADE, related_name='api_tokens', to='src.group')),
            ],
            options={
                'db_table': 'api_token',
            },
        ),
    ]
