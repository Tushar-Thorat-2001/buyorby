# Generated by Django 3.1.7 on 2021-03-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210328_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'TOP Wear'), ('BW', 'Bottom Wear'), ('ID', 'Indian'), ('D', 'Dress'), ('S', 'supplements'), ('E', 'equipments')], max_length=2),
        ),
    ]
