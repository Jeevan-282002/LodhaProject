# Generated by Django 4.1.5 on 2023-01-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LodhaApp', '0006_alter_reviewmodel_name_alter_reviewmodel_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='WT4BHKPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('month', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('password', models.IntegerField()),
            ],
        ),
    ]
