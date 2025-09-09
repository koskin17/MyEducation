import pytest
from django.db import IntegrityError
from profiles.models import ViewedStartup


@pytest.mark.django_db
def test_unique_constraint_on_viewed_startup(create_investor, create_startup):

    investor = create_investor(email="investor3@test.com", username="investor3")
    startup = create_startup(user=investor, company_name="Startup 3")

    ViewedStartup.objects.create(user=investor, startup=startup)
    with pytest.raises(IntegrityError):
        ViewedStartup.objects.create(user=investor, startup=startup)
