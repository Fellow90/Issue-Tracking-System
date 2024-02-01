# Generated by Django 4.2.5 on 2023-09-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0008_ticket_resolved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='resolved_by',
            field=models.CharField(blank=True, choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3')], max_length=2, null=True),
        ),
    ]