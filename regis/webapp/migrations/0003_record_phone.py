# Generated by Django 5.1.4 on 2024-12-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_record_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='phone',
            field=models.CharField(default=4, max_length=100),
            preserve_default=False,
        ),
    ]
