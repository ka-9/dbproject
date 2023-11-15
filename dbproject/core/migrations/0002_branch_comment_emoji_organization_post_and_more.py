# Generated by Django 4.1.1 on 2023-11-15 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branchID', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='branch_images/')),
                ('openingHours', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentID', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('emojiID', models.AutoField(primary_key=True, serialize=False)),
                ('emojiType', models.CharField(choices=[('HEART', 'HEART'), ('THUMB', 'THUMB'), ('FIRE', 'FIRE'), ('STAR', 'STAR')], max_length=255)),
                ('icon', models.ImageField(upload_to='emoji_icons/')),
                ('commentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('orgID', models.AutoField(primary_key=True, serialize=False)),
                ('orgName', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, upload_to='org_logos/')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postID', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='post_images/')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('isBookmarked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to='person_images/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_id',
            field=models.CharField(blank=True, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('plateNb', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('nbSeats', models.PositiveIntegerField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('tripID', models.AutoField(primary_key=True, serialize=False)),
                ('rideDate', models.DateTimeField()),
                ('nbParticipants', models.PositiveIntegerField()),
                ('departure', models.CharField(max_length=255)),
                ('isFeatured', models.BooleanField(default=False)),
                ('isBookmarked', models.BooleanField(default=False)),
                ('orgID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
                ('participants', models.ManyToManyField(blank=True, default='', null=True, related_name='participants', to='core.person')),
                ('plateNb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehicle')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stopID', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=500)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('isDestination', models.BooleanField()),
                ('branchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.branch')),
                ('tripID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trip')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comment')),
                ('emojiID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.emoji')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='personID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person'),
        ),
        migrations.AddField(
            model_name='post',
            name='tripID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trip'),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_friends', to='core.person')),
                ('personID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='core.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='personID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
        migrations.AddField(
            model_name='branch',
            name='orgID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization'),
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('adID', models.AutoField(primary_key=True, serialize=False)),
                ('duration', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('adLink', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='ad_images/')),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.organization')),
                ('branchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.branch')),
                ('postID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
