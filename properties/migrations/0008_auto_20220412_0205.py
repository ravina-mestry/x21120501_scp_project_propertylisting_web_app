# Generated by Django 2.0.2 on 2022-04-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_auto_20220411_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.CharField(choices=[('9', '9'), ('5', '5'), ('2', '2'), ('7', '7'), ('8', '8'), ('10+', '10+'), ('1', '1'), ('6', '6'), ('4', '4'), ('3', '3')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='property',
            name='ber_rating',
            field=models.CharField(choices=[('C3', 'C3'), ('A1', 'A1'), ('F', 'F'), ('B1', 'B1'), ('B3', 'B3'), ('A3', 'A3'), ('C1', 'C1'), ('C2', 'C2'), ('D2', 'D2'), ('E1', 'E1'), ('E2', 'E2'), ('G', 'G'), ('D1', 'D1'), ('A2', 'A2'), ('B2', 'B2')], default='A1', max_length=20),
        ),
        migrations.AlterField(
            model_name='property',
            name='county',
            field=models.CharField(choices=[('Derry', 'Derry'), ('Cavan', 'Cavan'), ('Cork', 'Cork'), ('Leitrim', 'Leitrim'), ('Limerick', 'Limerick'), ('Meath', 'Meath'), ('Sligo', 'Sligo'), ('Tipperary', 'Tipperary'), ('Carlow', 'Carlow'), ('Tyrone', 'Tyrone'), ('Monaghan', 'Monaghan'), ('Antrim', 'Antrim'), ('Kilkenny', 'Kilkenny'), ('Louth', 'Louth'), ('Westmeath', 'Westmeath'), ('Wicklow', 'Wicklow'), ('Roscommon', 'Roscommon'), ('Waterford', 'Waterford'), ('Longford', 'Longford'), ('Kildare', 'Kildare'), ('Galway', 'Galway'), ('Clare', 'Clare'), ('Laois', 'Laois'), ('Mayo', 'Mayo'), ('Down', 'Down'), ('Kerry', 'Kerry'), ('Fermanagh', 'Fermanagh'), ('Offaly', 'Offaly'), ('Wexford', 'Wexford'), ('Armagh', 'Armagh'), ('Dublin', 'Dublin'), ('Donegal', 'Donegal')], default='Carlow', max_length=12),
        ),
        migrations.AlterField(
            model_name='property',
            name='listing_type',
            field=models.CharField(choices=[('FOR LEASE', 'FOR LEASE'), ('FOR SALE', 'FOR SALE')], default='FOR SALE', max_length=20),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('DETACHED', 'DETACHED'), ('TERRACED', 'TERRACED'), ('BUNGALOW', 'BUNGALOW'), ('SITE', 'SITE'), ('SEMI-DETACHED', 'SEMI-DETACHED'), ('PARKING SPACE', 'PARKING SPACE'), ('APPARTMENT', 'APPARTMENT')], default='BUNGALOW', max_length=20),
        ),
    ]
