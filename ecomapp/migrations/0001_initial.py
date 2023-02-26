# Generated by Django 4.1.7 on 2023-02-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
    ]