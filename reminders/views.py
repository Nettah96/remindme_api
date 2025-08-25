from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import ModelSerializer
from .models import Reminder
from .serializers import ReminderSerializer

# ----------------------
# Reminder CRUD ViewSet
# ----------------------
class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return reminders owned by the logged-in user
        return self.request.user.reminders.all()

    def perform_create(self, serializer):
        # Attach the logged-in user when creating a reminder
        serializer.save(user=self.request.user)


# ----------------------
# User Registration
# ----------------------
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
