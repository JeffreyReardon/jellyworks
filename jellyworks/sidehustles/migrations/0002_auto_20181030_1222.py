# Generated by Django 2.1.2 on 2018-10-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidehustles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review_like_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review_star_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_proficiency',
            field=models.IntegerField(),
        ),
    ]
