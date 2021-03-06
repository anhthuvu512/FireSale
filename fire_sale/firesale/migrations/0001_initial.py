# Generated by Django 4.0.4 on 2022-05-13 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('highest_offer', models.IntegerField(blank=True, default=0)),
                ('condition', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('available', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('accepted', models.BooleanField(default=False)),
                ('message', models.CharField(blank=True, max_length=255)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.buyer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.item')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif', models.CharField(max_length=255)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.offer')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.seller')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.buyer')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.seller'),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(max_length=255, upload_to='images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.seller'),
        ),
        migrations.CreateModel(
            name='BuyerNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif', models.CharField(max_length=255)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.offer')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.buyer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firesale.seller')),
            ],
        ),
    ]
