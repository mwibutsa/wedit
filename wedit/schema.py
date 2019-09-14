import graphene
from wedit.apps.profiles.schema import profile_mutation
from wedit.apps.profiles.schema import profile_query


class Query(profile_query.Query, graphene.ObjectType):
    pass


class Mutation(profile_mutation.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
