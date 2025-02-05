from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_favorited_by_event_flagged_by_event_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='reason',
            field=models.CharField(choices=[('spam', 'Spam or Misleading'), ('abuse', 'Harassment or Abuse'), ('inappropriate', 'Inappropriate Content'), ('other', 'Other')], default='other', max_length=50),
        ),
    ]
