from django.db import models

# Create your models here.
MAX_LENGTH_CHAR = 255

class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название компании')
    agent_firstname = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Фамилия представителя')
    agent_name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Имя представителя')
    agent_patronymic = models.CharField(max_length=MAX_LENGTH_CHAR, null=True, verbose_name='Отчество представителя ')
    agent_telephone = models.CharField(max_length=MAX_LENGTH_CHAR, null=True, verbose_name='Телефон представителя')
    address = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Адрес поставщика')
    logical_del = models.BooleanField(default=True, verbose_name='Логическое удаление')

    def __str__(self):
        return f"{self.name} {self.agent_firstname} : {self.agent_telephone}"

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

        permissions = [
            ('change_address', 'Возможность изменения адреса поставщика'),
        ]


class Parametr(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Supply(models.Model):
    date_supply = models.DateTimeField(verbose_name='Дата поставки')

    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик')
    product = models.ManyToManyField('Product', through='Pos_supply', verbose_name='Товары')

    def __str__(self):
        return f"{self.pk} - {self.date_supply} {self.supplier.name}"

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class Order(models.Model):
    MAGAZINE="MG"
    COURIER="CR"
    PICKUPPOINT="PP"
    TYPE_DELIVERY = [
        (MAGAZINE, "Магазин"),
        (COURIER, "Курьер"),
        (PICKUPPOINT, "Пункт выдачи")

    ]

    FIO_customer = models.CharField(null=True, default='FIO', max_length=MAX_LENGTH_CHAR, verbose_name='ФИО покупателя')
    delivery_address = models.CharField(null=True, max_length=MAX_LENGTH_CHAR, verbose_name='Адресс доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=MAGAZINE, verbose_name='Способ доставки')
    date_create = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')

    books = models.ManyToManyField('Product', through='Pos_order')

    def __str__(self):
        return f'#{self.pk} {self.FIO_customer} - {self.date_create}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Pos_order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Продукт')
    order = models.ForeignKey('Order', on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество продукта')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на продукт')

    def __str__(self):
        return f'#{self.pk} {self.product.name} - {self.order.FIO_customer}'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название')
    description = models.TextField(null=True, blank=True,verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название товара')
    description = models.TextField(blank=True, null=True,verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    update_data = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления записи')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, verbose_name='Фотография товара')
    exists = models.BooleanField(default=True, verbose_name='Продается ли на данный момент?')

    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    tag = models.ManyToManyField('Tag', blank=True)
    parametr = models.ManyToManyField('Parametr', through='Pos_parametr')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Pos_parametr(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Продукт')
    parametr = models.ForeignKey('Parametr', on_delete=models.PROTECT, verbose_name='Характеристика')

    value = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Значение характеристики')

    def __str__(self):
        return f'{self.product.name} - {self.parametr.name} - {self.value}'

    class Meta:
        verbose_name = 'Позиция характеристики'
        verbose_name_plural = 'Позиции характеристик'
class Pos_supply(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Продукт')
    supply = models.ForeignKey('Supply', on_delete=models.PROTECT, verbose_name='Поставка')

    count = models.PositiveIntegerField(verbose_name='Количество товара')

    def __str__(self):
        return f'#{self.supply.pk} - {self.product.name}'

    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставок'