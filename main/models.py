from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, surname, phone, id_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not phone:
            raise ValueError("Users must provide a phone number")
        if not id_number:
            raise ValueError("Users must provide an ID number")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            surname=surname,
            phone=phone,
            id_number=id_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, surname, phone, id_number, password=None):
        user = self.create_user(email, first_name, last_name, surname, phone, id_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True)
    id_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    # Django required fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "surname", "phone", "id_number"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
