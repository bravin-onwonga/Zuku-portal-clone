from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from requests.auth import HTTPBasicAuth
import requests 
import json
import datetime
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from . models import MpesaPayment
from . forms import ShiftingRequestForm, ChangePackageForm
from . models import *
from django.template.loader import get_template
from . models import ShippingAddress
from django.contrib.auth.models import User

def home_view(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, creates = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'clients/home.html', context)

def store(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, creates = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'clients/store.html', context)

def cart(request):

	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'clients/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']
	submitted = False
	if request.method == "POST":
		form = CheckoutForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/package?submitted = True')
	else:
		form = CheckoutForm
		if 'submitted' in request.GET:
			submitted = True

	context = {'items':items, 'order':order, 'cartItems':cartItems, 'form': form, 'submitted': submitted}
	return render(request, 'clients/package.html', context)

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'clients/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:', action)
	print('productId:', productId)

	client = request.user.client
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(client=client, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id

		if total == order.get_cart_total/115.40:
			order.complete = True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
				client = client,
				order = order,
				address = data['shipping']['address'],
				city = data['shipping']['city'],
				phonenum = data['shipping']['phonenum'],
				zipcode = data['shipping']['zipcode'],
				)

	else:
		print('User is not logged in...')
	return JsonResponse('Payment complete!', safe=False)

def moving(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']
	submitted = False
	if request.method == "POST":
		form = ShiftingRequestForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/moving?submitted = True')
	else:
		form = ShiftingRequestForm
		if 'submitted' in request.GET:
			submitted = True

	context = {'items':items, 'order':order, 'cartItems':cartItems, 'form': form, 'submitted': submitted}
	return render(request, 'clients/moving.html', context)

def refer(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'clients/refer.html', context)

def receipt(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'clients/receipt.html', context)

def package(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	submitted = False
	if request.method == "POST":
		form = ChangePackageForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/package?submitted = True')
	else:
		form = ChangePackageForm
		if 'submitted' in request.GET:
			submitted = True

	context = {'items':items, 'order':order, 'cartItems':cartItems, 'form': form, 'submitted': submitted}
	return render(request, 'clients/package.html', context)

def ticket(request):
	if request.user.is_authenticated:
		client = request.user.client
		order, created = Order.objects.get_or_create(client=client, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'clients/ticket.html', context)

def getAccessToken(request):
	consumer_key = 'GvNwgmTqj6TA4cGXVzhvGa44MJ6kvz2a'
	consumer_secret = 'v0RE5VYb8XsBxA0C'
	api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

	r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
	mpesa_access_token = json.loads(r.text)
	validated_mpesa_access_token = mpesa_access_token['access_token']

	return HttpResponse(validated_mpesa_access_token)

def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254743909639,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254743909639,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Zuku",
        "TransactionDesc": "Testing stk push"
    }

    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponseRedirect('/store/')

@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Business_short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://2d47-41-81-128-44.eu.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://2d47-41-81-128-44.eu.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return redirect(request, 'clients/receipt.html')

@csrf_exempt
def call_back(request):
    pass

@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return redirect(request, 'clients/receipt.html')

@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return redirect(request, 'clients/receipt.html', context)