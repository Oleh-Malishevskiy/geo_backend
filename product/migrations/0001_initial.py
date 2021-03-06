# Generated by Django 4.0 on 2022-05-27 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('place', models.CharField(max_length=255)),
                ('depth', models.DecimalField(decimal_places=2, max_digits=6)),
                ('square', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenantsRN', to='product.building')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=255)),
                ('stat1', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stat2', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stat3', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stat4', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stat5', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
            ],
        ),
    ]
