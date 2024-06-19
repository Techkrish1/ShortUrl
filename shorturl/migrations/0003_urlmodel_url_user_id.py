# Generated by Django 4.2.5 on 2024-06-19 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0002_userdetail_alter_urlmodel_longurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlmodel',
            name='url_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shorturl.userdetail'),
        ),
    ]
