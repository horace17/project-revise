# Generated by Django 4.2 on 2024-11-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
