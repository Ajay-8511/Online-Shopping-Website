# Generated by Django 2.0.4 on 2018-05-22 15:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osm', '0002_auto_20180520_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller_product',
            name='seller_info_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller_product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='seller_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='osm.seller_info'),
        ),
        migrations.AlterField(
            model_name='address_info',
            name='mobile_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='mobile_detail',
            name='mobile_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d[0-9]*$')]),
        ),
        migrations.DeleteModel(
            name='seller_product',
        ),
    ]