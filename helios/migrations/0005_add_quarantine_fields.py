# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Election.complaint_period_ends_at'
        db.add_column('helios_election', 'complaint_period_ends_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True), keep_default=False)

        # Adding field 'CastVote.quarantined_p'
        db.add_column('helios_castvote', 'quarantined_p', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'CastVote.released_from_quarantine_at'
        db.add_column('helios_castvote', 'released_from_quarantine_at', self.gf('django.db.models.fields.DateTimeField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Election.complaint_period_ends_at'
        db.delete_column('helios_election', 'complaint_period_ends_at')

        # Deleting field 'CastVote.quarantined_p'
        db.delete_column('helios_castvote', 'quarantined_p')

        # Deleting field 'CastVote.released_from_quarantine_at'
        db.delete_column('helios_castvote', 'released_from_quarantine_at')


    models = {
        'helios_auth.user': {
            'Meta': {'unique_together': "(('user_type', 'user_id'),)", 'object_name': 'User'},
            'admin_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('helios_auth.jsonfield.JSONField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'token': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'helios.auditedballot': {
            'Meta': {'object_name': 'AuditedBallot'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_vote': ('django.db.models.fields.TextField', [], {}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'helios.castvote': {
            'Meta': {'object_name': 'CastVote'},
            'cast_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invalidated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'quarantined_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'released_from_quarantine_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'verified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'vote': ('helios_auth.jsonfield.JSONField', [], {}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vote_tinyhash': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Voter']"})
        },
        'helios.election': {
            'Meta': {'object_name': 'Election'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios_auth.User']"}),
            'archived_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'cast_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'complaint_period_ends_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datatype': ('django.db.models.fields.CharField', [], {'default': "'legacy/Election'", 'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'election_type': ('django.db.models.fields.CharField', [], {'default': "'election'", 'max_length': '250'}),
            'eligibility': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'encrypted_tally': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'featured_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frozen_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'openreg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'private_key': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'private_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public_key': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'questions': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'registration_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'result': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'result_proof': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tallies_combined_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_finished_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'use_advanced_audit_features': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_voter_aliases': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'voters_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voting_ended_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_ends_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_extended_until': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'})
        },
        'helios.electionlog': {
            'Meta': {'object_name': 'ElectionLog'},
            'at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'helios.trustee': {
            'Meta': {'object_name': 'Trustee'},
            'decryption_factors': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'decryption_proofs': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pok': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'public_key': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'public_key_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secret_key': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'helios.voter': {
            'Meta': {'object_name': 'Voter'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'cast_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios_auth.User']", 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vote': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voter_email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'voter_login_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voter_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'voter_password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        'helios.voterfile': {
            'Meta': {'object_name': 'VoterFile'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['helios.Election']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_voters': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'processing_finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'processing_started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'voter_file': ('django.db.models.fields.files.FileField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['helios']
