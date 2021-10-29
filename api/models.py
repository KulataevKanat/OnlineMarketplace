from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from OnlineMarketplace import settings
from OnlineMarketplace.advice import STATUS_NONE, PURCHASED
from OnlineMarketplace.models import BaseModel
from api.managers import UserAccountManager


class User(BaseModel, AbstractUser):
    id = models.AutoField(primary_key=True)
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=False, blank=True, null=True)
    is_supplier = models.BooleanField(_('supplier'), default=False)

    objects = UserAccountManager()

    REQUIRED_FIELDS = ['groups_id', 'email']
    USERNAME_FIELD = 'username'
    REQUIRED_ADMIN_FIELDS = ['email']

    def __str__(self):
        return self.username.__str__()

    def get_short_name(self):
        return self.first_name

    class Meta:
        db_table = 'api_user'
        verbose_name = _('Пользоваетель')
        verbose_name_plural = _('Пользователи')


class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Product(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, default='product_title')
    description = models.CharField(max_length=500, blank=True, default='product_description')
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    supplier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class Comments(BaseModel):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    # rate
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=300, blank=True, default='text')
    relplies = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='add_relplies')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product')

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')


class Cart(BaseModel):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_id')
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(blank=False, default=0)

    class Meta:
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')


class Orders(BaseModel):
    PRODUCT_STATUS = (
        (STATUS_NONE, _('None')),
        (PURCHASED, _('Куплено')),
    )
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    # address
    # phone
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=PRODUCT_STATUS, max_length=100, blank=True, null=True,
                              default=STATUS_NONE)

    class Meta:
        verbose_name = _('Продуктовая операция')
        verbose_name_plural = _('Продуктовые операции')


class ProductHistory(BaseModel):
    id = models.AutoField(primary_key=True)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True, blank=True,
                               related_name="orders")
    prod_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="prod_id")
    name = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, default='product_title')
    description = models.CharField(max_length=500, blank=True, default='product_description')
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.IntegerField(blank=False, default=0)

    class Meta:
        verbose_name = _('История продукта')
        verbose_name_plural = _('Истории продуктов')
