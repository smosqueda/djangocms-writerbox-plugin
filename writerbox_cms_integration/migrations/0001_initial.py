# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionChoicePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='writerbox_cms_integration_sectionchoicepluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('section', models.ForeignKey(to='writer.Section')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
