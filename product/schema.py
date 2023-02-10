import graphene
from graphene_django import DjangoObjectType

from .models import Product, Category, Gallery, Included, MiniProduct
from images.models import CategoryImage, ProductImage


class CategoryImageType(DjangoObjectType):
    def resolve_image(self, info):
        """Resolve product image absolute path"""
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image

    class Meta:
        model = CategoryImage


class ProductImageType(DjangoObjectType):
    def resolve_desktop(self, info):
        """Resolve product image absolute path"""
        if self.desktop:
            self.desktop = info.context.build_absolute_uri(self.desktop.url)
        return self.desktop

    def resolve_tablet(self, info):
        """Resolve product image absolute path"""
        if self.tablet:
            self.tablet = info.context.build_absolute_uri(self.tablet.url)
        return self.tablet

    def resolve_mobile(self, info):
        """Resolve product image absolute path"""
        if self.mobile:
            self.mobile = info.context.build_absolute_uri(self.mobile.url)
        return self.mobile

    class Meta:
        model = ProductImage


class GalleryType(DjangoObjectType):
    class Meta:
        model = Gallery


class IncludedType(DjangoObjectType):
    class Meta:
        model = Included


class MiniProductType(DjangoObjectType):
    class Meta:
        model = MiniProduct


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        exclude = ["orderNumber"]


class ProductQuery(graphene.ObjectType):
    all_categories = graphene.List(CategoryType, description="Returns all categories")
    category_by_slug = graphene.Field(
        CategoryType,
        slug=graphene.String(required=True),
        description="Returns specific category",
    )
    all_products = graphene.List(ProductType, description="Returns all Products")
    product_by_slug = graphene.Field(
        ProductType,
        slug=graphene.String(required=True),
        description="Get product by Slug",
    )

    def resolve_all_categories(self, info: any) -> any:
        return Category.objects.all()

    def resolve_category_by_slug(self, info, slug):
        return Category.objects.get(slug=slug)

    def resolve_all_products(self, info):
        return Product.objects.all()

    def resolve_product_by_slug(self, info, slug):
        return Product.objects.get(slug=slug)
