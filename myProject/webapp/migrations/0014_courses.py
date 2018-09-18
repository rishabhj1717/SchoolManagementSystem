# Generated by Django 2.1 on 2018-09-16 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courseName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sem', models.IntegerField(blank=True, default=0, null=True)),
                ('deptName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Department')),
            ],
        ),
    ]