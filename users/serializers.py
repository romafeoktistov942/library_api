from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "password",
            "first_name",
            "last_name",
            "is_active",
            "email",
            "phone",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        """
        Переопределяем метод для контроля отображения полей
        """
        ret = super().to_representation(instance)
        request = self.context.get("request")

        if not request or not request.user.is_superuser:
            if not request.user == instance:
                ret.pop("password", None)

        return ret
