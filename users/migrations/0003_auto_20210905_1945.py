# Generated by Django 3.2.5 on 2021-09-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_chronicdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='coviddata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Breathing', models.IntegerField()),
                ('Problem', models.IntegerField()),
                ('Fever', models.IntegerField()),
                ('Dry_Cough', models.IntegerField()),
                ('Sore_throat', models.IntegerField()),
                ('Running_ose', models.IntegerField()),
                ('Asthma', models.IntegerField()),
                ('Chronic_Lung_Disease', models.IntegerField()),
                ('Headache', models.IntegerField()),
                ('Heart_Disease', models.IntegerField()),
                ('Diabetes', models.IntegerField()),
                ('Hyper_Tension', models.IntegerField()),
                ('Fatigue', models.IntegerField()),
                ('Gastro', models.IntegerField()),
                ('Abroad_travel', models.IntegerField()),
                ('Contact_with_COVID_Patient', models.IntegerField()),
                ('Attended_Large_Gathering', models.IntegerField()),
                ('Visited_Public_Exposed_Places', models.IntegerField()),
                ('Family_working_in_Public_Exposed_Places', models.IntegerField()),
                ('Wearing_Masks', models.IntegerField()),
                ('Sanitization_from_Market', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='chronicdata',
            name='Sickle_Cell',
            field=models.FloatField(),
        ),
    ]
