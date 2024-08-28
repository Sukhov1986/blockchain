# Generated by Django 5.0.7 on 2024-08-15 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dialog',
            options={'ordering': ['-created']},
        ),
        migrations.AlterUniqueTogether(
            name='dialog',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.AddField(
            model_name='dialog',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dialogs_as_user1', to='users.profile'),
        ),
        migrations.AddField(
            model_name='dialog',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dialogs_as_user2', to='users.profile'),
        ),
        migrations.RemoveField(
            model_name='dialog',
            name='participant1',
        ),
        migrations.RemoveField(
            model_name='dialog',
            name='participant2',
        ),
    ]
