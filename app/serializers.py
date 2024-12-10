from rest_framework import serializers

class CSVUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField(required=True)
    keys = serializers.CharField(required=False, allow_blank=True)
    colored = serializers.BooleanField(default=True)