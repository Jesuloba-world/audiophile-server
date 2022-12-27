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

    def resolve_user_cart(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise UnauthorisedAccessError(message="You are not authenticated")
        else:
            return CartItem.objects.filter(owner=user)


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


class RemoveAllCartMutations(graphene.Mutation):
    class Arguments:
        pass

    success = graphene.Field(graphene.Boolean)

    @classmethod
    def mutate(cls, root, info):
        user = info.context.user

        if user.is_anonymous:
            raise UnauthorisedAccessError(message="You are not authenticated")
        else:
            all_cart_items = CartItem.objects.filter(owner=user)
            all_cart_items.delete()
            return RemoveAllCartMutations(success=True)


class DeleteCartMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    success = graphene.Field(graphene.Boolean)

    @classmethod
    def mutate(cls, root, info, id):
        user = info.context.user

        if user.is_anonymous:
            raise UnauthorisedAccessError(message="You are not authenticated")
        else:
            cart_item = CartItem.objects.get(pk=id)
            cart_item.delete()
            return DeleteCartMutation(success=True)


class CartMutations(graphene.ObjectType):
    add_to_cart = AddCartMutation.Field()
    remove_all_cart = RemoveAllCartMutations.Field()
    delete_from_cart = DeleteCartMutation.Field()
