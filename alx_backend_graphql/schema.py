import graphene
from crm.schema import Query as CRMQuery, Mutation as CRMMutation

class Query(CRMQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")
    pass

class Mutation(CRMMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

class UpdateLowStockProducts(graphene.Mutation):
    class Arguments:
        pass

    success = graphene.String()
    updated_products = graphene.List(ProductType)

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated_products = []

        for product in low_stock_products:
            product.stock += 10  #restocking
            product.save()
            updated_products.append(product)

        message = f"{len(updated_products)} products updated successfully."
        return UpdateLowStockProducts(success=message, updated_products=updated_products)


class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

#schema includes mutation
schema = graphene.Schema(mutation=Mutation)

