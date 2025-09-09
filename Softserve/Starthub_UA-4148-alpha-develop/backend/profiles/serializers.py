from rest_framework import serializers
from .models import ViewedStartup, StartupProfile


class StartupProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupProfile
        fields = [
            "id",
            "company_name",
            "description",
            "website",
            "views_count",
            "industry",
            "location",
        ]


class ViewedStartupSerializer(serializers.ModelSerializer):
    startup_id = serializers.IntegerField(source="startup.id", read_only=True)
    company_name = serializers.CharField(source="startup.company_name", read_only=True)

    class Meta:
        model = ViewedStartup
        fields = ["startup_id", "company_name", "viewed_at"]
