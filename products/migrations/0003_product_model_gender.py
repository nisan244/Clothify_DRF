# Generated by Django 5.1.3 on 2025-01-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_model_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_model',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], max_length=20, null=True),
        ),
    ]
