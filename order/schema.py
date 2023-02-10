import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Order, OrderAddress, OrderProduct
from product.models import Product
from cart.models import CartItem


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


class OrderAddressInput(graphene.InputObjectType):
    class Meta:
        description = "Input type for the OrderAddress object."

    name = graphene.String(required=True)
    email_address = graphene.String(required=True)
    phone_number = graphene.String(required=True)
    address = graphene.String(required=True)
    zipcode = graphene.String(required=True)
    city = graphene.String(required=True)
    country = graphene.String(required=True)


class OrderQuery(graphene.ObjectType):
    my_order = graphene.List(OrderType, description="get all order related to a user")

    def resolve_my_order(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise UnauthorisedAccessError(message="You are not authenticated")
        else:
            return Order.objects.filter(owner=user)


class NewOrderMutation(graphene.Mutation):
    class Arguments:
        address = OrderAddressInput(required=True)
        paymentMethod = graphene.String(required=True)

    order = graphene.Field(OrderType)
    success = graphene.Field(graphene.Boolean)

    @classmethod
    def mutate(cls, root, info, address, paymentMethod):
        user = info.context.user

        if user.is_anonymous:
            raise UnauthorisedAccessError(message="You are not authenticated")
        else:
            try:
                # create order
                order = Order.objects.create(owner=user, paymentMethod=paymentMethod)
                # add the address
                OrderAddress.objects.create(
                    name=address.name,
                    email_address=address.email_address,
                    phone_number=address.phone_number,
                    address=address.address,
                    zipcode=address.zipcode,
                    city=address.city,
                    country=address.country,
                    order=order,
                )
                # get cartItems
                cartItems = CartItem.objects.filter(owner=user)

                # use the gotten cartItems to create orderProducts and delete cartitem
                for item in cartItems:
                    OrderProduct.objects.create(
                        product=item.product, order=order, quantity=item.quantity
                    )
                    item.delete()

                return cls(order=order, success=True)
            except Exception as e:
                print(e)
                return cls(success=False)


class OrderMutations(graphene.ObjectType):
    new_order = NewOrderMutation.Field()
