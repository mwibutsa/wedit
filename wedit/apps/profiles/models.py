from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class ProfileManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        """ Creates and saves a user with the given email and password. """

        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have username')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        """ Creates and saves staff user. """

        user = self.create_user(email, username, password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password=None):
        """ Creates and saves super user. """

        user = self.create_user(email, username, password=password)
        user.staff = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(unique=True, null=False, max_length=60)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = ProfileManager()

    def get_full_name(self):
        """ Returns the user's full name """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """ Returns the user's short name """
        return f"{self.first_name}"

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Check if the user has permission on certain object """
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        """ Check if the user is a member of staff. """
        return self.staff

    @property
    def is_admin(self):
        """ Check if the user is a member of staff. """
        return self.admin

    @property
    def is_active(self):
        """ Check if the user is a member of staff. """
        return self.active
