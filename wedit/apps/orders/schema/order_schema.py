from wedit.apps.orders.models import Order
from graphene_django import DjangoObjectType


class OrderType(DjangoObjectType):
    class Meta:
        model = Order
