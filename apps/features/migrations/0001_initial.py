# Generated by Django 4.1.5 on 2024-05-12 03:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering_number', models.PositiveSmallIntegerField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='categories.category')),
                ('sub_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='categories.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=1, default=0, max_digits=20)),
                ('value', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='features.feature')),
            ],
            options={
                'unique_together': {('feature', 'value')},
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('feature_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.featurevalue')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'unique_together': {('product', 'feature_value')},
            },
        ),
    ]
