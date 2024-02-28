from rest_framework import serializers


class FibonacciSerializer(serializers.Serializer):
    steps = serializers.IntegerField()

    def validate_steps(self, value):
        if value < 1:
            raise serializers.ValidationError('An integer greater than zero is required.')
        return value