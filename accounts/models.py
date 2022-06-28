from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **Kwargs):
        if username is None:
            raise TypeError("Users should have a username")
        if email is None:
            raise TypeError("Users should have a Email")
        user = self.model(
            username=username, email=self.normalize_email(email), **Kwargs
        )
        user.set_password(password)
        user.is_staff = True
        user.save()

        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError("Password should not be none")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {
    "facebook": "facebook",
    "google": "google",
    "twitter": "twitter",
    "email": "email",
}


class User(AbstractBaseUser, PermissionsMixin):
    def upload_to(instance, filename):
        return "{filename}".format(filename=filename)

    is_company = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=32, default=False)
    profile_img = models.ImageField(
        max_length=None, upload_to=upload_to, default="photos/adham-img_Lh0ntBw.jpg"
    )
    card_id_img = models.ImageField(
        max_length=None, upload_to=upload_to, default="photos/adham-img_Lh0ntBw.jpg"
    )
    commercial_record_img = models.ImageField(
        max_length=None, upload_to=upload_to, default="photos/adham-img_Lh0ntBw.jpg"
    )
    country = models.CharField(max_length=32, default=False)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=32, default='example' )
    last_name = models.CharField(max_length=32, default='example')
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    
    last_login = models.DateTimeField(auto_now=True )
    auth_provider = models.CharField(
        max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get("email")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
