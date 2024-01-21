from rest_framework import serializers

from user.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('image', )
