# Generated by Django 3.2.6 on 2021-10-07 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Address_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Address_Province', models.CharField(max_length=50)),
                ('Address_City', models.CharField(max_length=50)),
                ('Address_Street', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('Driver_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Driver_FirstName', models.CharField(max_length=50)),
                ('Driver_LastName', models.CharField(max_length=50)),
                ('Driver_Password', models.CharField(max_length=50)),
                ('Driver_Email', models.EmailField(max_length=50)),
                ('Address_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.address')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('Food_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Food_Name', models.CharField(max_length=50)),
                ('Food_Desc', models.CharField(max_length=100)),
                ('Food_Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('User_FirstName', models.CharField(max_length=50)),
                ('User_LastName', models.CharField(max_length=50)),
                ('User_Password', models.CharField(max_length=50)),
                ('User_ContactNumber', models.CharField(max_length=50)),
                ('User_Email', models.EmailField(max_length=50, unique=True)),
                ('Address_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.address')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('Restaurant_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Restaurant_Name', models.CharField(max_length=50)),
                ('Restaurant_Desc', models.CharField(max_length=100)),
                ('Restaurant_ContactNumber', models.CharField(max_length=50)),
                ('Address_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.address')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('Order_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('Cost', models.IntegerField()),
                ('Food_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.food')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Order_Type', models.CharField(max_length=50)),
                ('Order_TotalCost', models.IntegerField()),
                ('Driver_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.driver')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.user')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='Restaurant_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.restaurant'),
        ),
    ]
