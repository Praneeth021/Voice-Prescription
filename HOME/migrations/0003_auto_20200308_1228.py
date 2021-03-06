# Generated by Django 3.0.1 on 2020-03-08 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0002_complaint_doctor_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phoneno',
            field=models.BigIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Description', models.TextField()),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HOME.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HOME.Patient')),
            ],
        ),
    ]
