# Generated by Django 5.1.3 on 2025-02-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_model_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_model',
            name='image',
            field=models.ImageField(null=True, upload_to='category/image/'),
        ),
    ]
