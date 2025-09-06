

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesave',
            name='hints_used',
            field=models.IntegerField(default=0),
        ),
    ]
