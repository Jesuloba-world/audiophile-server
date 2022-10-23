from pyexpat import model
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from product.models import Product

from .models import CartItem


class UnauthorisedAccessError(GraphQLError):
    def __init__(self, message, *args, **kwargs):
        super(UnauthorisedAccessError, self).__init__(message, *args, **kwargs)


class CartItemType(DjangoObjectType):
    class Meta:
        model = CartItem


class CartQuery(graphene.ObjectType):
    user_cart = graphene.List(
        CartItemType,
        description="return user cart items",
    )


class AddCartMutation(graphene.Mutation):
    class Arguments:
        product_id = graphene.String(required=True)
        quantity = graphene.Int(required=True)

    cartItem = graphene.Field(CartItemType)

    @classmethod
    def mutate(cls, root, info, product_id, quantity):
        user = info.context.user
        cart_product = Product.objects.get(id=product_id)

        if user.is_anonymous:
            raise UnauthorisedAccessError(message="You are not authenticated")
        else:
            (new_cart_item, created) = CartItem.objects.update_or_create(
                product=cart_product, owner=user, defaults={"quantity": quantity}
            )
            return AddCartMutation(cartItem=new_cart_item)


class CartMutations(graphene.ObjectType):
    add_to_cart = AddCartMutation.Field()
