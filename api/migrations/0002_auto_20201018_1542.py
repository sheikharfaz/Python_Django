# Generated by Django 3.0.8 on 2020-10-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestreservation',
            name='roomNumber',
        ),
        migrations.AddField(
            model_name='hotelmodel',
            name='Room_availability',
            field=models.CharField(choices=[('empty', 'Empty'), ('Occupied', 'Occupied')], default='empty', max_length=100),
        ),
        migrations.AddField(
            model_name='hotelmodel',
            name='Room_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hotelmodel',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.DeleteModel(
            name='RoomAvailable',
        ),
    ]