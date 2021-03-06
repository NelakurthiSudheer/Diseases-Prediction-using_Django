# Generated by Django 3.2.5 on 2021-09-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='heartdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField()),
                ('Gender', models.IntegerField()),
                ('Constrictive_pericarditis', models.IntegerField()),
                ('Resting_Blood_Pressure', models.IntegerField()),
                ('Serum_Cholesterol', models.IntegerField()),
                ('Fasting_Blood_Pressure', models.IntegerField()),
                ('Restecg', models.IntegerField()),
                ('Maximum_Heart_Rate_Achieved', models.IntegerField()),
                ('Exercise_Induced_Angina', models.IntegerField()),
                ('Exercise_Relative_To_Rest', models.IntegerField()),
                ('Speech_Language_Pathologist', models.IntegerField()),
                ('Coronary_Artery_Anomaly', models.IntegerField()),
                ('Thalassemia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=67)),
                ('password', models.CharField(max_length=67)),
                ('username', models.CharField(max_length=89)),
            ],
        ),
    ]
