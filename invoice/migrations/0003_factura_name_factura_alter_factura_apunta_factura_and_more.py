# Generated by Django 5.1 on 2024-09-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_alter_factura_tipo_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='name_factura',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='apunta_factura',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='tipo_factura',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
