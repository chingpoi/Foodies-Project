# Generated by Django 3.2.6 on 2021-10-09 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodies', '0004_auto_20211009_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='Order_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='foodies.order'),
            preserve_default=False,
        ),
    ]
