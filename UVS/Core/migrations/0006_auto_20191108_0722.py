# Generated by Django 2.2.6 on 2019-11-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_contest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('voting ongoing', 'voting ongoing'), ('registration ongoing', 'registration ongoing'), ('registration ended', 'registration ended'), ('results relesed', 'results relesed'), ('ended', 'ended')], default='active', max_length=50),
        ),
    ]
