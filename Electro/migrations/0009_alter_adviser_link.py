# Generated by Django 5.0.6 on 2024-06-11 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electro', '0008_alter_banner_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adviser',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
