from django .urls import path
from . import views

app.name - 'Ecommerce'

urlpatterns - [
path('', views.product_list, names='product_list')

]