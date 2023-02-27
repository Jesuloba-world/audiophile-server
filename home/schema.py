import graphene
from graphene_django import DjangoObjectType

from .models import Hero


class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class HomeQuery(graphene.ObjectType):
    hero = graphene.Field(HeroType, description="The hero section")

    def resolve_hero(self, info):
        return Hero.objects.get()
