import graphene
from wedit.apps.profiles.schema import profile_mutation
from wedit.apps.profiles.schema import profile_query
import graphql_jwt
from wedit.apps.profiles.schema import profile_schema


class Query(profile_query.Query, graphene.ObjectType):
    pass


class ObtainJSONWebTOken(graphql_jwt.JSONWebTokenMutation):

    user = graphene.Field(profile_schema.ProfileType)

    class Meta:
        excludes = ['password']

    @classmethod
    def resolve(self, root, info, **kwargs):
        return self(user=info.context.user)


class Mutation(profile_mutation.Mutation, graphene.ObjectType):
    login = ObtainJSONWebTOken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
