# Generated by Ginger 5.3.4 on 2024-08-04 09:14

from ginger.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_package_remove_service_lang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='lang',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
