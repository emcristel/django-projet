# Generated by Django 4.0.4 on 2022-04-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oeuvre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('creation', models.DateField(blank=True, null=True)),
                ('type_oeuvre', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
