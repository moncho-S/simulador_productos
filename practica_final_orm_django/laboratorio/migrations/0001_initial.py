# Generated by Django 4.1.1 on 2023-07-25 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'laboratorio',
                'verbose_name_plural': 'laboratorios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('f_fabricacion', models.DateField()),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('p_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
            options={
                'verbose_name': 'Director General',
                'verbose_name_plural': 'Director Generals',
            },
        ),
    ]
