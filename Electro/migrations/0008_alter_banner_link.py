# Generated by Django 5.0.6 on 2024-06-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electro', '0007_adviser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]