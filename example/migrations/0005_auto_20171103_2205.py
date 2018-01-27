# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 22:05
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.fields
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0004_auto_20171019_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='body',
            field=wagtail.core.fields.StreamField((('rich_text', wagtail.core.blocks.RichTextBlock()), ('form', wagtail.core.blocks.StructBlock((('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False))))))),
        ),
    ]
