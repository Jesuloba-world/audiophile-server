import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Order, OrderAddress, OrderProduct


class UnauthorisedAccessError(GraphQLError):
    def __init__(self, message, *args, **kwargs):
        super(UnauthorisedAccessError, self).__init__(message, *args, **kwargs)


class OrderType(DjangoObjectType):
    class Meta:
        model = Order


class OrderAddressType(DjangoObjectType):
    class Meta:
        model = OrderAddress


class OrderProductType(DjangoObjectType):
    class Meta:
        model = OrderProduct
        exclude = ["order"]


class OrderQuery(graphene.ObjectType):
    my_order = graphene.List(OrderType, description="get all order related to a user")

    def resolve_my_order(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise UnauthorisedAccessError(message="You are not authenticated")
        else:
            return Order.objects.filter(owner=user)


class OrderMutation:
    pass
