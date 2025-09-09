from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Industry(models.Model):
    """Represents an industry sector that a startup can belong to."""

    INDUSTRY_CHOICES = [
        ("category 1", "category 1"),
        ("category 2", "category 2"),
        ("category 3", "category 3"),
        ("category 4", "category 4"),
        ("category 5", "category 5"),
        ("category 6", "category 6"),
        ("category 7", "category 7"),
        ("category 8", "category 8"),
    ]

    name = models.CharField(max_length=100, choices=INDUSTRY_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """Represents a geographical location of a startup."""

    LOCATION_CHOICES = [
        ("Autonomous Republic of Crimea", "Autonomous Republic of Crimea"),
        ("Lviv Oblast", "Lviv Oblast"),
        ("Ivano-Frankivsk Oblast", "Ivano-Frankivsk Oblast"),
        ("Odesa Oblast", "Odesa Oblast"),
        ("Rivne Oblast", "Rivne Oblast"),
        ("Ternopil Oblast", "Ternopil Oblast"),
        ("Sumy Oblast", "Sumy Oblast"),
        ("Kyiv Oblast", "Kyiv Oblast"),
    ]

    name = models.CharField(max_length=100, choices=LOCATION_CHOICES, unique=True)

    def __str__(self):
        return self.name


class StartupProfile(models.Model):
    """Profile for a startup, including company info, industry, and location."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="startups"
    )
    company_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    views_count = models.IntegerField(default=0)
    industry = models.ForeignKey(
        Industry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="startups",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="startup_locations",
    )

    def __str__(self):
        return self.company_name


class InvestorProfile(models.Model):
    """Profile for an investor, including company info and website."""

    user = models.OneToOneField(  # Change user = models.ForeignKey on user = models.OneToOneField in class InvestorProfile in profiles/models because Django does not automatically create the user.investorprofile attribute for ForeignKey
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="investorprofile",
    )
    company_name = models.CharField(max_length=150, blank=True)
    website = models.URLField(blank=True)

    saved_projects = models.ManyToManyField(
        "projects.StartupProject",
        through="projects.SavedProject",
        related_name="saved_entries",
    )

    def __str__(self):
        return self.company_name or self.user.username


class ViewedStartup(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="viewed_startups",
        limit_choices_to={"role__role": "investor"},  # only investors can be selected
    )
    startup = models.ForeignKey(
        StartupProfile, on_delete=models.CASCADE, related_name="views"
    )
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "startup"], name="unique_investor_startup_view"
            )
        ]
        ordering = ["-viewed_at"]

    def __str__(self):
        return (
            f"{self.user.email} viewed {self.startup.company_name} on {self.viewed_at}"
        )
