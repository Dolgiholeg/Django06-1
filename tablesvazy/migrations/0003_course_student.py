# Generated by Django 4.2.5 on 2023-09-13 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablesvazy', '0002_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('group', models.CharField(max_length=4)),
                ('course', models.ManyToManyField(to='tablesvazy.course')),
            ],
        ),
    ]
