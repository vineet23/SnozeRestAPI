from rest_framework import serializers
from Songs.models import Song

class Song_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields=('__all__')