# Generated by Django 3.0.1 on 2020-03-18 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0007_complaint_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HOME.Doctor'),
            preserve_default=False,
        ),
    ]
