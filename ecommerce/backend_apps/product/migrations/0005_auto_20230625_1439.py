# Generated by Django 3.2 on 2023-06-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20230625_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=31, upload_to='product_images'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
