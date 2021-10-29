from rest_framework import serializers


class NotSerializer(serializers.Serializer, object):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
