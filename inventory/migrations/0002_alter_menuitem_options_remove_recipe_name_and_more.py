# Generated by Django 4.0.4 on 2022-05-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='name',
        ),
        migrations.AddField(
            model_name='recipe',
            name='unit',
            field=models.CharField(choices=[('kg', 'kg'), ('gr', 'gr'), ('ltr', 'liter'), ('tbs', 'tbs'), ('tsp', 'tsp')], default='gr', max_length=4),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('kg', 'kg'), ('gr', 'gr'), ('ltr', 'liter'), ('tbs', 'tbs'), ('tsp', 'tsp')], default='gr', max_length=4),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=15),
        ),
    ]
