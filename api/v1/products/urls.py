from django.urls import path, re_path
from . import views

app_name = "api_v1_accounts"


urlpatterns = [
    re_path(r'^offer-product/$', views.offered_products, name="offer_products"),
]
