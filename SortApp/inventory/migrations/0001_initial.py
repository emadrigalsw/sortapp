# Generated by Django 4.1.5 on 2023-01-19 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('quantity', models.FloatField(default=0.0)),
                ('unit', models.CharField(choices=[('PD', 'Pounds'), ('KG', 'Kilograms'), ('GR', 'Grams'), ('ML', 'Milliliters'), ('LT', 'Liters')], max_length=2)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ingredient')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.menuitem')),
            ],
        ),
    ]
