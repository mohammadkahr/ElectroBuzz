# Generated by Django 5.0.6 on 2024-06-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electro', '0005_alter_banner_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='caption',
            field=models.CharField(max_length=1000),
        ),
    ]
