# Generated by Django 2.1.4 on 2019-03-02 20:49

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('crop_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_month', django.contrib.postgres.fields.jsonb.JSONField()),
                ('end_month', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='CropFamily',
            fields=[
                ('family_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_id_pk', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('picture_link', models.CharField(max_length=2000)),
                ('symptoms', django.contrib.postgres.fields.jsonb.JSONField()),
                ('crops_affected', django.contrib.postgres.fields.jsonb.JSONField()),
                ('treatment', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('farm_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('bio', models.CharField(max_length=2000)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', django.contrib.postgres.fields.jsonb.JSONField()),
                ('crops_grown', django.contrib.postgres.fields.jsonb.JSONField()),
                ('interested_in_selling', models.BooleanField()),
                ('contact', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='family_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.CropFamily'),
        ),
    ]
