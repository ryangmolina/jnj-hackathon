from django.contrib.auth.models import AbstractUser
from django.db import models

from app.core import models as core_models
from .managers import AccountManager


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    username = models.CharField(
        max_length=24,
        unique=False,
        blank=True,
    )

    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email


class Profile(core_models.BaseModel):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    unit = models.CharField(max_length=64, blank=True, null=True)
    street = models.CharField(max_length=64, blank=True, null=True)
    zip_code = models.CharField(max_length=64, blank=True, null=True)

    gender = models.CharField(max_length=64, blank=True, choices=GENDER)
    civil_status = models.CharField(max_length=64, blank=True)
    province = models.CharField(max_length=64, blank=True)
    city_municipality = models.CharField(max_length=64, blank=True)
    highest_educational_attainment = models.CharField(max_length=64, blank=True)
    educational_status = models.CharField(max_length=64, blank=True)
    tenure = models.FloatField()
    employment_status = models.CharField(max_length=64, blank=True)
    pay_class = models.CharField(max_length=64, blank=True)
    last_employee_movement = models.CharField(max_length=64, blank=True)
    latest_performance_rating = models.CharField(max_length=64, blank=True)
    job_loc = models.CharField(max_length=64, blank=True)
    rank = models.CharField(max_length=64, blank=True)
    job_unit = models.CharField(max_length=64, blank=True)
