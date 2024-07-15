# from django.db import models
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.utils import timezone


# class UserManager(BaseUserManager):

#     def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
#         now = timezone.now()
#         if not email:
#             raise ValueError(('The email must be set'))
#         email = self.normalize_email(email)
#         user = self.model(email=email, is_staff=is_staff, 
#                           is_active=True, is_superuser=is_superuser,
#                           last_login=now, created_at=now, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_user(self, email=None, password=None, **extra_fields):
#         return self._create_user(email, password, False, False, ' ', **extra_fields)
    
#     def create_superuser(self, email, password, **extra_fields):
#         user = self._create_user(email, password, True, True, **extra_fields)
#         user.is_active = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.CharField(max_length=250, unique=True)
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     phone = models.CharField(max_length=30, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     created_at = models.DateTimeField(default=timezone.now)
#     country = models.CharField(max_length=30, blank=True, null=True)
#     city = models.CharField(max_length=30, blank=True, null=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email', ]
