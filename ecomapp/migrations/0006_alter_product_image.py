# Generated by Django 4.1.7 on 2023-02-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_order_lineitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='media/default.png', upload_to='media'),
        ),
    ]