from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "due_date",
            "status",
            "priority",
            "user",
        ]
        read_only_fields = ["id", "created_at", "user"]
