# Generated by Django 3.2 on 2022-01-22 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated date')),
                ('label', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated date')),
                ('label', models.CharField(max_length=300, unique=True)),
                ('status', models.CharField(choices=[('n', 'new'), ('p', 'process'), ('s', 'send')], max_length=1)),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='app_wh.warehouse', verbose_name='Warehouse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
