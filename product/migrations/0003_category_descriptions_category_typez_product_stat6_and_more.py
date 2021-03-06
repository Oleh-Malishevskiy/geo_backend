# Generated by Django 4.0 on 2022-05-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_name_product_date_category_lat_category_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='descriptions',
            field=models.TextField(default=3, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='typez',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stat6',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stat7',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=3, upload_to=''),
            preserve_default=False,
        ),
    ]
