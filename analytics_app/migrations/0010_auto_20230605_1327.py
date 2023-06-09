# Generated by Django 3.2.19 on 2023-06-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_app', '0009_rename_useractivity_visitoractivity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitoractivity',
            old_name='device_type',
            new_name='device',
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='browser_family',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='browser_version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='device_family',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='is_mobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='is_pc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='is_tablet',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='os_family',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='visitoractivity',
            name='os_version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
