from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    price = models.FloatField(verbose_name=_("Price"))

    def __str__(self):
        return self.title


class Order(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_users", verbose_name=_("User"))
    amount = models.PositiveIntegerField(verbose_name=_("Amount"))

    def __str__(self):
        return f"{self.user} - {self.product}"


class Providers(BaseModel):
    class ProviderChoices(models.TextChoices):
        PAYME = "payme", _("Payme")
        PAYLOV = 'paylov', _("Paylov")
        CLICK = 'click', _("Click")
        UZUM = 'uzum', _("Uzum")

    provider = models.CharField(max_length=255, choices=ProviderChoices.choices, verbose_name=_("Provider"))
    key = models.CharField(max_length=255, verbose_name=_("Key"))
    key_description = models.CharField(max_length=255, verbose_name=_("Key description"))
    value = models.CharField(max_length=255, verbose_name=_("Value"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    class Meta:
        unique_together = ("provider", "key")
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")


class Transaction(models.Model):
    class StatusType(models.TextChoices):
        PENDING = 'pending', _('Pending')
        ACCEPTED = 'accepted', _('Accepted')
        REJECTED = 'rejected', _('Rejected')
        CANCELED = 'canceled', _('Canceled')

    amount = models.DecimalField(_('Amount'), max_digits=10, decimal_places=2)
    status = models.CharField(_('Status'), max_length=32, choices=StatusType.choices, default=StatusType.PENDING)
    remote_id = models.CharField(_('Remote id'), max_length=255, null=True, blank=True)
    paid_at = models.DateTimeField(verbose_name=_("Paid at"), null=True, blank=True)
    canceled_at = models.DateTimeField(verbose_name=_("Canceled at"), null=True, blank=True)
    extra = models.JSONField(_('Extra'), null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("Order"))
    provider = models.CharField(choices=Providers.ProviderChoices.choices, blank=True, null=True, max_length=15)
    is_paid_with_card = models.BooleanField(default=False, verbose_name=_("Is paid with card ?"))
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        db_table = 'Transaction'
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        ordering = ('remote_id',)
