# Generated by Django 3.2.4 on 2021-07-07 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Supplier', '0002_auto_20210707_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companyj'},
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Supplier.company', verbose_name='companyj'),
        ),
    ]
