# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 17:32
from __future__ import unicode_literals

from django.db import migrations, transaction


def transfer_tags(apps, schema_editor):
    """Transfer existing relations between Alerts and Tags to TagRelations."""
    Alert = apps.get_model('alerts', 'Alert')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    TagRelation = apps.get_model('tags', 'TagRelation')
    while Alert.objects.filter(tags__isnull=False).exists():
        with transaction.atomic():
            for alert in Alert.objects.filter(tags__isnull=False)[:1000]:
                print(alert)
                for tag in alert.tags.all():
                    model_type = ContentType.objects.get_for_model(alert)
                    TagRelation.objects.create(
                        content_type=model_type,
                        object_id=alert.id,
                        tag=tag
                    )
                    alert.tags.clear()


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('tags', '0002_auto_20170810_1608'),
        ('alerts', '0008_auto_20170807_1103'),
    ]

    operations = [
        migrations.RunPython(
            transfer_tags,
            reverse_code=migrations.RunPython.noop
        ),
    ]
