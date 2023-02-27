import graphene
from graphene_django import DjangoObjectType

from .models import Hero, FeaturedProduct


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class FeaturedProductType(DjangoObjectType):
    class Meta:
        model = FeaturedProduct


class HomeQuery(graphene.ObjectType):
    hero = graphene.Field(HeroType, description="The hero section")
    featured_products = graphene.List(
        FeaturedProductType, description="This will return all featured products"
    )

    def resolve_hero(self, info):
        return Hero.objects.get()

    def resolve_featured_products(self, info):
        return FeaturedProduct.objects.all()
