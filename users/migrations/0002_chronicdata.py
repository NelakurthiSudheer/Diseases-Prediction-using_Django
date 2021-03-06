# Generated by Django 3.2.5 on 2021-09-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chronicdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField()),
                ('Blood_Pressure', models.IntegerField()),
                ('Urinary_specific_gravity', models.IntegerField()),
                ('AL', models.IntegerField()),
                ('STROKE_UNIT', models.IntegerField()),
                ('Red_Blood_Cells', models.IntegerField()),
                ('Post_Cibum', models.IntegerField()),
                ('Protein_C_Cofactor', models.IntegerField()),
                ('Blood_Alcohol', models.IntegerField()),
                ('Blood_Glucose_Regulator', models.IntegerField()),
                ('Blood_Unit', models.IntegerField()),
                ('Sickle_Cell', models.IntegerField()),
                ('Sphincter_Of_Oddi_Dysfunction', models.IntegerField()),
                ('Postural_tachycardia_syndrome', models.IntegerField()),
                ('Hemoglobin', models.IntegerField()),
                ('Packed_Cell_Volume', models.IntegerField()),
                ('White_Cells', models.IntegerField()),
                ('Respiratory_Congestion', models.IntegerField()),
                ('HYPERTENSION', models.IntegerField()),
                ('Diabetes_Mellitus', models.IntegerField()),
                ('Coronary_Artery_Disease', models.IntegerField()),
                ('Appetite', models.IntegerField()),
                ('Pulmonary_Embolism', models.IntegerField()),
                ('Acute_Necrotizing_Encephalopathy', models.IntegerField()),
            ],
        ),
    ]
