# Generated by Django 5.0.3 on 2024-08-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_company_price_hour_factura_labour_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoiceline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_id', models.BigIntegerField(null=True)),
                ('company_id', models.BigIntegerField(null=True)),
                ('article_id', models.BigIntegerField(null=True)),
                ('article_name', models.CharField(max_length=111, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
            options={
                'indexes': [models.Index(fields=['company_id'], name='invoice_inv_company_ecdc24_idx'), models.Index(fields=['invoice_id'], name='invoice_inv_invoice_166710_idx')],
            },
        ),
    ]
