from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Contact(models.Model):
    """ Модель контакта """

    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=100, verbose_name='номер дома')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Supplier(models.Model):
    """ Модель поставщика """

    name = models.CharField(max_length=100, verbose_name='название')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Network(models.Model):
    """ Модель сети поставщиков """

    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=100, verbose_name='название')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='звено сети')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'


class Product(models.Model):
    """ Модель продукта """

    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name='звено сети')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='время создания', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
