from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addToCart", views.addToCart, name="addToCart"),
    path("shopping_cart", views.shopping_cart_view, name="shopping_cart_view"),
    path("checkout", views.checkout, name="checkout"),
    path("orders_list", views.orders_list, name="orders_list"),
    path("completeOrder", views.completeOrder, name="completeOrder"),
    path("register", views.register_view_get, name="register_view_get"),
    path("register_post", views.register_view_post, name="register_view_post"),
    path("login", views.login_view_get, name="login_view_get"),
    path("login_post", views.login_view_post, name="login_view_post"),
    path("logout", views.logout_view, name="logout")
]
