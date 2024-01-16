# Generated by Django 3.0.5 on 2021-11-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0005_auto_20211128_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(null=True, to='bazaar.Category'),
        ),
    ]