# Generated by Django 3.0.1 on 2020-03-21 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0009_auto_20200321_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='complaint',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='HOME.Complaint'),
        ),
    ]
