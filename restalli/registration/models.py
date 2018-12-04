from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
import uuid
from comun.models import Estados

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, perfil, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Debe agregar un Email')

        user = self.model(
            email=self.normalize_email(email),
            perfil=perfil,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, perfil, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            perfil=perfil,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    MANAGER = 'MNG'
    MESERO = 'MSR'
    CAJERO = 'CJA'
    
    PERFIL_CHOICES = (
        (MANAGER, 'Administrador'),
        (MESERO, 'Mesero'),
        (CAJERO, 'Cajero'),
        
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='perfiles', null= True, blank= True)
    perfil = models.CharField(
        max_length=3,
        choices=PERFIL_CHOICES,
        default=MESERO,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['perfil']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "El usuario tiene permiso?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "EL usuario tiene permiso para ver el modulo `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "es un usuario administrador?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
