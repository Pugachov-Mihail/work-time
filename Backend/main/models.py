from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ShopName(models.Model):
    name = models.CharField(unique=True, max_length=25, null=True, blank=False, verbose_name="Название торговой точки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Название торговой точки"


class PersonalShope(AbstractUser):
    workShop = models.ForeignKey(ShopName, on_delete=models.PROTECT, null=True, blank=False, verbose_name="Сотрудник торговой точки")
    is_active = models.BooleanField(default=True)

    class Meta(AbstractUser.Meta):
        verbose_name_plural = "Сотрудники магазина"


class PlansMonth(models.Model):
    shopname = models.ForeignKey(ShopName, on_delete=models.CASCADE, verbose_name='Название ТТ')
    metal = models.IntegerField(null=False, blank=False,verbose_name="Железо")
    accs = models.IntegerField(null=False, blank=False,verbose_name="Аксы")
    dop = models.IntegerField(null=False, blank=False,verbose_name="Доп оборот")
    oss = models.IntegerField(null=False, blank=False,verbose_name="ОСС")
    setting = models.IntegerField(null=False, blank=False,verbose_name="Настройки")
    bil = models.IntegerField(null=False, blank=False,verbose_name="Билайн")
    mega = models.IntegerField(null=False, blank=False,verbose_name="Мегафон")
    yota = models.IntegerField(null=False, blank=False,verbose_name="Yota")
    tele = models.IntegerField(null=False, blank=False,verbose_name="Теле 2")
    persone = models.IntegerField(null=False, blank=False,verbose_name="Сотрудников")
    date = models.DateTimeField(null=False, blank=False,auto_now=True)

    def __str__(self):
        return ("Планы торговой точки: " + self.shopname.name)

    class Meta:
        verbose_name_plural = "Планы на день"