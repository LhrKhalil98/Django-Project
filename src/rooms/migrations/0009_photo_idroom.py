# Generated by Django 2.2 on 2019-04-27 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_remove_photo_idroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='idRoom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
    ]
