# Generated by Django 3.2.7 on 2021-11-15 18:09

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20211115_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='brands', validators=[catalog.validators.validate_brand], verbose_name='Изображение')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.brand')),
            ],
        ),
    ]
