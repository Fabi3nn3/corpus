# Generated by Django 2.0 on 2018-08-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_page_annotation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebPageAnnotationAppWebPageAnnotationModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('korpus_id', models.IntegerField()),
                ('hit', models.IntegerField()),
                ('task', models.IntegerField()),
                ('ad_mace', models.CharField(max_length=250)),
                ('ad_annotation', models.CharField(default='-', max_length=250)),
                ('cutoff_mace', models.CharField(max_length=250)),
                ('cutoff_annotation', models.CharField(default='-', max_length=250)),
                ('loading_mace', models.CharField(max_length=250)),
                ('loading_annotation', models.CharField(default='-', max_length=250)),
                ('pornographic_mace', models.CharField(max_length=250)),
                ('pornographic_annotation', models.CharField(default='-', max_length=250)),
                ('popup_mace', models.CharField(max_length=250)),
                ('popup_annotation', models.CharField(default='-', max_length=250)),
                ('captcha_mace', models.CharField(max_length=250)),
                ('captcha_annotation', models.CharField(default='-', max_length=250)),
                ('error_mace', models.CharField(max_length=250)),
                ('error_annotation', models.CharField(default='-', max_length=250)),
            ],
            options={
                'managed': True,
                'db_table': 'web_page_annotation_app_web_page_annotation_model',
            },
        ),
    ]
