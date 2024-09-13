from rest_framework import serializers

from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(source='payments_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'payments')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
