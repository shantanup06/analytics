# Generated by Django 3.2.19 on 2023-05-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_app', '0006_useractivity_page_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='page_type',
            field=models.CharField(blank=True, choices=[('HT', 'Hit'), ('SF', 'Surf'), ('EX', 'Exit')], max_length=2, null=True),
        ),
    ]
