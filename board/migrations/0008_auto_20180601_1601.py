# Generated by Django 2.0.5 on 2018-06-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20180530_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='board.Item'),
        ),
    ]