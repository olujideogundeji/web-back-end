# Generated by Django 3.0.6 on 2020-06-07 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20200605_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('text', models.CharField(max_length=255)),
                ('parent_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
