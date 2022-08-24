from django.urls import path
from . import views

urlpatterns = [
	path("home/", views.home_view, name = "home"),
	path("store/", views.store, name = "store"),
	path("cart/", views.cart, name = "cart"),
	path("checkout/", views.checkout, name = "checkout"),
	path("receipt/", views.receipt, name = "receipt" ),
	path("moving/", views.moving, name = "moving"),
	path("refer/", views.refer, name = "refer"),
	path("package/", views.package, name="package"),
	path("package/", views.package, name="validate"),
	path("ticket/", views.ticket, name="ticket"),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

    # register, confirmation, validation and callback urls
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
	
	path("update_item/", views.updateItem, name="update_item"),
	path("process_order/", views.processOrder, name="process_order"),
]
