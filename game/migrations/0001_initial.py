

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('algorithm', models.CharField(max_length=20)),
                ('difficulty', models.CharField(max_length=10)),
                ('current_array', models.TextField()),
                ('original_array', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('moves', models.IntegerField(default=0)),
                ('step', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
