import graphene
from wedit.apps.orders.models import Order
from graphql_jwt.decorators import login_required


class CreateOrder(graphene.Mutation):

    """ Mutation to create orders. """
    owner = graphene.String()
    order_title = graphene.String()
    order_summary = graphene.String()
    order_file = graphene.String()
    description_file = graphene.String()

    class Arguments:
        order_title = graphene.String()
        order_summary = graphene.String()
        order_file = graphene.String()
        description_file = graphene.String()

    @login_required
    def mutate(self, info, order_title, order_summary, order_file, description_file):
        order = Order(
            order_title=order_file,
            order_summary=order_summary,
            order_file=order_file,
            description_file=description_file
        )
        order.owner = info.context.user
        order.save()

        return CreateOrder(
            owner=order.owner.username,
            order_title=order.order_title,
            order_summary=order.order_summary,
            order_file=order.order_file,
            description_file=order.description_file
        )


class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
