from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated date')

    class Meta:
        abstract = True


class Warehouse(BaseModel):
    label = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.label


class Order(BaseModel):
    STATUS_CHOICES = (
        ('n', 'new'),
        ('p', 'process'),
        ('s', 'send'),
    )
    label = models.CharField(max_length=300, unique=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    warehouse = models.ForeignKey(Warehouse, verbose_name='Warehouse', on_delete=models.PROTECT,
                                  related_name='order')

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        # self.current_authenticated_user
        super(Order, self).save(*args, **kwargs)
