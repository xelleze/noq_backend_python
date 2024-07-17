# Generated by Django 4.2.10 on 2024-07-17 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_booking_booking_time_booking_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('paid', models.BooleanField(default=False)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('currency', models.CharField(default='SEK', max_length=3)),
                ('invoice_number', models.CharField(max_length=50, unique=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='backend.host')),
            ],
        ),
    ]
