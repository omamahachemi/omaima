from django.contrib import admin
from .models import Customer, Invoice, Article

# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'sex', 'age', 'city', 'zip_code')

class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'saved_by', 'invoice_date_time', 'last_updated_date', 'paid', 'invoice_type')

admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article)  # Assuming you want to register Article model too
