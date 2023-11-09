from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class UserClass(models.TextChoices):
        INVESTOR = 'Investor', ('Investor')
        WVC = 'WVC', ('Wealth Voyage Counselor')

    user_class = models.CharField(
        max_length=20,
        choices=UserClass.choices,
        default=UserClass.INVESTOR,
    )
