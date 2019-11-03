# Generated by Django 2.2.6 on 2019-11-03 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WR', 'Waiting for reply'), ('FR', 'Friends')], default='WR', max_length=2, verbose_name='Friendship status')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='init_friendship', to=settings.AUTH_USER_MODEL, verbose_name='Initiator')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replied_friendship', to=settings.AUTH_USER_MODEL, verbose_name='Replier')),
            ],
            options={
                'verbose_name': 'friendship',
                'verbose_name_plural': 'friendships',
            },
        ),
    ]
