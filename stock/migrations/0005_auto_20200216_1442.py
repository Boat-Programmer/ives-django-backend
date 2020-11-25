# Generated by Django 3.0.3 on 2020-02-16 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0004_auto_20200215_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='firstname',
            field=models.CharField(max_length=50, verbose_name='Firstname'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastname',
            field=models.CharField(max_length=50, verbose_name='Lastname'),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
