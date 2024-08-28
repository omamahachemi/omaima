from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    """
    Name: Customer model definition
    """
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    name = models.CharField(max_length=132)
    email = models.EmailField()
    phone = models.CharField(max_length=132)
    address = models.CharField(max_length=64)
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    age = models.CharField(max_length=12)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    created_date = models.DateTimeField(auto_now_add=True)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.name}_{self.created_date}"

    @property
    def get_total(self):
        articles = self.article_set.all()
        total = sum(article.get_total for article in articles)
        return total


class Invoice(models.Model):
    """
    Name: Invoice model definition
    Description:
    author: donbdjdhk@njb.com
    """
    INVOICE_TYPE = (
        ('R', 'RECU'),
        ('P', 'PROFORMA FACTURE'),
        ('F', 'FACTURE'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    saved_by = models.ForeignKey(User, on_delete=models.PROTECT)
    invoice_date_time = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated_date = models.DateTimeField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'


class Article(models.Model):
    """
    Name: Article model definition
    Description:
    author: donbdjdhk@njb.com
    """
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    @property
    def get_total(self):
        return self.quantity * self.unit_price
