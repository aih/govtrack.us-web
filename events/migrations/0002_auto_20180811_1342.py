# Generated by Django 2.0.8 on 2018-08-11 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.Feed'),
        ),
        migrations.AlterField(
            model_name='event',
            name='source_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='subscriptionlist',
            name='email',
            field=models.IntegerField(choices=[(0, 'No Email Updates'), (1, 'Daily'), (2, 'Weekly')], default=0),
        ),
    ]