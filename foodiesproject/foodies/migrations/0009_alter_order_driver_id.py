# Generated by Django 3.2.6 on 2021-10-09 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodies', '0008_alter_order_driver_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Driver_ID',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='foodies.driver'),
        ),
    ]
