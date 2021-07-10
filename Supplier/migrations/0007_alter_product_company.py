# Generated by Django 3.2.4 on 2021-07-08 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0006_auto_20210708_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_product', to='Supplier.company'),
        ),
    ]