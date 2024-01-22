from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    """ Роли пользователей. """

    MEMBER = 'member', _('member')
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser):
    """ Модель пользователя """

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=200, verbose_name='имя')
    last_name = models.CharField(max_length=200, verbose_name='фамилия')
    role = models.CharField(
        max_length=6,
        choices=UserRoles.choices,
        default=UserRoles.MEMBER,
        verbose_name='роль пользователя'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.MEMBER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
