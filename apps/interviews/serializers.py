from rest_framework import serializers


class AvailableInterviewSlotsSerializers(serializers.Serializer):
    studentId = serializers.IntegerField()
    startDateTime = serializers.DateTimeField()
    endDateTime = serializers.DateTimeField()
