# Generated by Django 4.0.4 on 2022-04-16 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='categ_relate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='market.category'),
            preserve_default=False,
        ),
    ]
