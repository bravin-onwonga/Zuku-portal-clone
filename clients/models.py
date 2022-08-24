from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
	client = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField()
	digital = models.BooleanField(default=False, null=True, blank=False)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	

class Order(models.Model):
	client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping
	

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	
class ShippingAddress(models.Model):
	client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	phonenum = models.IntegerField(null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class ShiftingRequest(models.Model):
	name = models.CharField(max_length=200, null=True)
	account = models.IntegerField(null=True)
	email = models.EmailField(max_length=200, null=True)
	phonenumber = models.IntegerField(null=True)
	caretaker = models.IntegerField(null=True)
	streetname = models.CharField(max_length=200, null=True)
	bname = models.CharField(max_length=200, null=True)
	landmark = models.CharField(max_length=200, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.streetname

class Tickets(models.Model):
	client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
	account = models.IntegerField(null=True)
	email = models.EmailField(max_length=200, null=True)
	phonenumber = models.IntegerField(null = True)
	description = models.CharField(max_length = 255, null= True)

	def __str__(self):
		return self.account

class ChangePackage(models.Model):
	account = models.IntegerField(null=True)
	email = models.EmailField(max_length=200, null=True)
	package_type = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.package_type

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# M-pesa Payment models

class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'


class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'


class MpesaPayment(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'

    def __str__(self):
        return self.first_name

class Checkout(models.Model):
	client_number = models.IntegerField(null = True)
	address = models.CharField(max_length=200, null=True)
	zipcode = models.IntegerField(null=True)
	landmark2 = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.address