# Generated by Django 5.1.3 on 2025-03-17 09:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('provider', models.CharField(choices=[('payme', 'Payme'), ('paylov', 'Paylov'), ('click', 'Click'), ('uzum', 'Uzum')], max_length=255, verbose_name='Provider')),
                ('key', models.CharField(max_length=255, verbose_name='Key')),
                ('key_description', models.CharField(max_length=255, verbose_name='Key description')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Provider',
                'verbose_name_plural': 'Providers',
                'unique_together': {('provider', 'key')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('canceled', 'Canceled')], default='pending', max_length=32, verbose_name='Status')),
                ('remote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Remote id')),
                ('paid_at', models.DateTimeField(blank=True, null=True, verbose_name='Paid at')),
                ('canceled_at', models.DateTimeField(blank=True, null=True, verbose_name='Canceled at')),
                ('extra', models.JSONField(blank=True, null=True, verbose_name='Extra')),
                ('provider', models.CharField(blank=True, choices=[('payme', 'Payme'), ('paylov', 'Paylov'), ('click', 'Click'), ('uzum', 'Uzum')], max_length=15, null=True)),
                ('is_paid_with_card', models.BooleanField(default=False, verbose_name='Is paid with card ?')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'Transaction',
                'ordering': ('remote_id',),
            },
        ),
    ]
