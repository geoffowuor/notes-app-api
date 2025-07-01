from django.contrib.auth.models import Group, User
from .models import Note
from rest_framework import serializers

class NoteSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content', 'created_at', 'updated_at']
