# Generated by Django 5.1.4 on 2025-02-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_userinfo_clientview'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='url_tracking_data',
            field=models.JSONField(default=dict),
        ),
    ]
