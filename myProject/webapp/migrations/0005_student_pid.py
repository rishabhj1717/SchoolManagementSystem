# Generated by Django 2.1 on 2018-09-14 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='webapp.Parent'),
        ),
    ]