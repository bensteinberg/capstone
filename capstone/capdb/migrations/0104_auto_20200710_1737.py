# Generated by Django 2.2.13 on 2020-07-10 17:37

import capdb.versioning
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0103_auto_20200618_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagestructure',
            name='sys_period',
            field=capdb.versioning.DefaultDateTimeRangeField(),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HistoricalPageStructure',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('order', models.SmallIntegerField()),
                ('label', models.CharField(blank=True, max_length=100)),
                ('blocks', django.contrib.postgres.fields.jsonb.JSONField()),
                ('spaces', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('font_names', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('encrypted_strings', models.TextField(blank=True, null=True)),
                ('duplicates', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('extra_redacted_ids', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('image_file_name', models.CharField(max_length=100)),
                ('width', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('deskew', models.CharField(blank=True, max_length=1000)),
                ('ingest_path', models.CharField(max_length=1000)),
                ('sys_period', capdb.versioning.DefaultDateTimeRangeField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('ingest_source', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='capdb.TarFile')),
                ('volume', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='capdb.VolumeMetadata')),
            ],
            options={
                'get_latest_by': 'history_date',
                'ordering': ('-sys_period', '-history_id'),
                'verbose_name': 'historical page structure',
                'db_table': 'capdb_pagestructure_history',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]