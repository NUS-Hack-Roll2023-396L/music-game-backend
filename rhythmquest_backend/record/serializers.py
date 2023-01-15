from record.models import MusicRecord
from rest_framework import serializers


class MusicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicRecord
