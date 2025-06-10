import time
import datetime
import pytz
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator

ROLE_CHOICES = (
    (0, 'visitor'),
    (1, 'admin'),
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, middle_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          first_name=first_name,
                          middle_name=middle_name,
                          last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.created_at = timezone.now()
        user.updated_at = timezone.now()
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=100, validators=[EmailValidator()])
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'middle_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return (
            f"'id': {self.id}, "
            f"'first_name': '{self.first_name}', "
            f"'middle_name': '{self.middle_name}', "
            f"'last_name': '{self.last_name}', "
            f"'email': '{self.email}', "
            f"'created_at': {int(self.created_at.timestamp())}, "
            f"'updated_at': {int(self.updated_at.timestamp())}, "
            f"'role': {self.role}, "
            f"'is_active': {self.is_active}"
        )

    def __repr__(self):
        return f"CustomUser(id={self.id})"

    @staticmethod
    def get_by_id(user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def get_by_email(email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            user.delete()
            return True
        except CustomUser.DoesNotExist:
            return False

    @staticmethod
    def create(email, password, first_name=None, middle_name=None, last_name=None, **kwargs):
        # Забороняємо створення з роллю через цей метод
        if 'role' in kwargs:
            raise TypeError('Role cannot be specified in create method')

        # Перевірка довжини імен
        if first_name and len(first_name) > 20:
            return None
        if middle_name and len(middle_name) > 20:
            return None
        if last_name and len(last_name) > 20:
            return None

        # Перевірка валідності email (проста, використовується валідатор в полі)
        from django.core.exceptions import ValidationError
        from django.core.validators import validate_email
        try:
            validate_email(email)
        except ValidationError:
            return None

        # Перевірка унікальності email
        if CustomUser.objects.filter(email=email).exists():
            return None

        user = CustomUser.objects.create_user(email=email,
                                              password=password,
                                              first_name=first_name or '',
                                              middle_name=middle_name or '',
                                              last_name=last_name or '')
        return user

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': int(self.created_at.timestamp()),
            'updated_at': int(self.updated_at.timestamp()),
            'role': self.role,
            'is_active': self.is_active,
        }

    def update(self,
               first_name=None,
               last_name=None,
               middle_name=None,
               password=None,
               role=None,
               is_active=None):
        updated = False
        if first_name is not None:
            self.first_name = first_name
            updated = True
        if middle_name is not None:
            self.middle_name = middle_name
            updated = True
        if last_name is not None:
            self.last_name = last_name
            updated = True
        if password is not None:
            self.set_password(password)
            updated = True
        if role is not None:
            self.role = role
            updated = True
        if is_active is not None:
            self.is_active = is_active
            updated = True

        if updated:
            self.updated_at = timezone.now()
            self.save()

    @staticmethod
    def get_all():
        return CustomUser.objects.all()

    def get_role_name(self):
        return dict(ROLE_CHOICES).get(self.role, 'unknown')
