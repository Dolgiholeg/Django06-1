# Generated by Django 4.2.5 on 2023-09-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablesvazy', '0004_user_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='packaging',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='recommended',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='volume',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
