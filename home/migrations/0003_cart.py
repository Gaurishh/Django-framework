# Generated by Django 3.2.12 on 2022-11-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221120_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('product_desc', models.CharField(max_length=200)),
                ('image', models.ImageField(default='', upload_to='static/img')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]