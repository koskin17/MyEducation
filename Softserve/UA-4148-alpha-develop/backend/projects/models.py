from django.db import models
from django.conf import settings
from profiles.models import StartupProfile, InvestorProfile


class StartupProject(models.Model):
    """Represents a project created by a startup, including investment details."""

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        FUNDED = "FUNDED", "Funded"

    subject = models.CharField(max_length=150)
    idea = models.TextField()
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    investment_needed = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    startup = models.ForeignKey(
        StartupProfile, on_delete=models.CASCADE, related_name="projects"
    )
    investor = models.ForeignKey(
        InvestorProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="investments",
    )
    funding_goal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.subject

    def total_funding(self):
        return sum(sub.share for sub in self.subscriptions.all())

    def remaining_funding(self):
        if self.funding_goal is None:
            return None
        return self.funding_goal - self.total_funding()


class SavedProject(models.Model):
    """Intermediate table for represents a project saved by investor (many-to-many relation)."""

    investor = models.ForeignKey(
        InvestorProfile,
        on_delete=models.CASCADE,
        related_name="investor_saved_projects",
    )
    project = models.ForeignKey(
        StartupProject, on_delete=models.CASCADE, related_name="saved_by_investors"
    )
    saved_at = models.DateTimeField(
        auto_now_add=True, help_text="Date and time the project was saved"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["investor", "project"], name="uniq_investor_project"
            )  # one investor cannot save same project twice
        ]
        ordering = ["-saved_at"]
        verbose_name = "Saved project"
        verbose_name_plural = "Saved projects"

    def __str__(self):
        return f"{self.investor.company_name} saved project {self.project.subject} from {self.project.startup.company_name}"


class Subscription(models.Model):
    project = models.ForeignKey(
        StartupProject, on_delete=models.CASCADE, related_name="subscriptions"
    )
    investor = models.ForeignKey(
        InvestorProfile, on_delete=models.CASCADE, related_name="subscriptions"
    )
    share = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor} -> {self.project} ({self.share})"


class ProjectRevision(models.Model):
    project = models.ForeignKey(
        StartupProject, on_delete=models.CASCADE, related_name="revisions"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    changes = models.JSONField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Revision of {self.project.subject} at {self.updated_at}"
