# Generated by Django 4.1.2 on 2022-10-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_dt', models.DateTimeField(auto_now=True)),
                ('order_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('order_phone', models.CharField(max_length=200, verbose_name='Телефон')),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
