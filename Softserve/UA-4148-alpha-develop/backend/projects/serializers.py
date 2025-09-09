from rest_framework import serializers
from .models import StartupProject, Subscription


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the StartupProject model.

    Provides a read-only representation of a startup project, including related
    fields such as the project's status, startup name, and investor name.
    """

    status = serializers.CharField(read_only=True)
    startup_name = serializers.CharField(source="startup.company_name", read_only=True)
    investor_name = serializers.CharField(
        source="investor.company_name", read_only=True, default=None
    )

    class Meta:
        model = StartupProject
        fields = [
            "id",
            "subject",
            "idea",
            "description",
            "website",
            "investment_needed",
            "views_count",
            "created_at",
            "updated_at",
            "status",
            "startup_name",
            "investor_name",
        ]

    def validate_subject(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Subject must be at least 3 characters long."
            )
        return value

    def validate_idea(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Idea cannot be empty.")
        return value


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["id", "project", "share"]

    def validate(self, data):
        project = data["project"]
        share = data["share"]

        if not hasattr(project, "funding_goal") or project.funding_goal is None:
            raise serializers.ValidationError("This project has no funding goal set.")

        if project.remaining_funding() < share:
            raise serializers.ValidationError(
                "Funding goal already reached or share too high."
            )

        return data
