# Generated by Django 4.2.1 on 2023-05-30 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recurringpayment',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='recurringpayment',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='budget.paymentcategory'),
        ),
        migrations.AlterField(
            model_name='recurringpayment',
            name='url',
            field=models.URLField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
