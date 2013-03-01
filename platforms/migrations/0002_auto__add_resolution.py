# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resolution'
        db.create_table(u'platforms_resolution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('platform', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['platforms.Platform'])),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('subdomain', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('uripattern', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'platforms', ['Resolution'])


    def backwards(self, orm):
        # Deleting model 'Resolution'
        db.delete_table(u'platforms_resolution')


    models = {
        u'platforms.platform': {
            'Meta': {'object_name': 'Platform'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'platforms.resolution': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Resolution'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['platforms.Platform']"}),
            'subdomain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'uripattern': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['platforms']