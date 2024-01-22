from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """ Кастомный менеджер для модели пользователя. """
    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password=None):
        """ Функция создания обычного пользователя. """
        if not email:
            raise ValueError('Поле email должно быть заполнено.')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role='member'
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """ Функция создания суперпользователя. """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_superuser=True,
            role='admin'
        )

        user.save(using=self._db)
        return user
