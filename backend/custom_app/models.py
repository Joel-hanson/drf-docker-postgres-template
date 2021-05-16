from django.db import models
from datetime import datetime, date
from django.core.exceptions import ValidationError


# Create your models here.
class Product(models.Model):
    TELEVISION = 1
    REFRIGERATOR = 2
    CATEGORY = (
        (TELEVISION, "Television"),
        (REFRIGERATOR, "Refrigerator"),
    )
    category = models.IntegerField(default=TELEVISION, choices=CATEGORY)
    model_no = models.TextField("model number of the product", null=False, blank=False)
    available = models.IntegerField("available product number", null=False, blank=False)
    price = models.FloatField("price of the product", null=False, blank=False)

    class Meta:
        unique_together = (
            "category",
            "model_no",
        )

    def __str__(self):
        return "{} - {}".format(self.get_category_display(), self.model_no)


class Team(models.Model):
    team_name = models.TextField("The team name", null=False, blank=False, unique=True)
    idle_from = models.DateTimeField(
        "The time since team was idle", null=True, blank=True
    )

    def __str__(self):
        return self.team_name


class Order(models.Model):
    order_number = models.CharField(
        max_length=9, null=True, blank=False
    )
    name = models.CharField(
        "name of the customer", max_length=256, null=True, blank=False
    )
    address = models.TextField("address of the customer", null=True, blank=False)
    distance = models.FloatField("distance of delivery address", null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        date_prefix = datetime.now().strftime("%d%m%y_")
        slno = Order.objects.filter(created_at__startswith=date.today()).count()
        self.order_number = date_prefix + str(slno + 1).zfill(2)
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, verbose_name="related product", on_delete=models.DO_NOTHING
    )
    quantity = models.IntegerField("number of items bought", null=False, blank=False)
    order = models.ForeignKey(
        Order, verbose_name="related order", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            "product",
            "order",
        )

    def __str__(self):
        return str(self.order.id)

    def save(self, *args, **kwargs):
        if self.product.available <= 0:
            raise ValidationError("The product is now available. The available count is zero")
        else:
            super().save(*args, **kwargs)
            self.product.available = self.product.available - 1
            self.product.save()
