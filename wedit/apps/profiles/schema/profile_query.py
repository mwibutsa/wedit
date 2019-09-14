from wedit.apps.profiles.schema.profile_schema import ProfileType
import graphene
from graphene_django import DjangoObjectType
from wedit.apps.profiles.models import Profile
from graphql import GraphQLError


class Query(graphene.ObjectType):
    users = graphene.List(ProfileType)
    user = graphene.Field(
        ProfileType, username=graphene.String(), email=graphene.String())

    def resolve_users(self, info, **kwargs):
        return Profile.objects.all()

    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        if username:
            return Profile.objects.filter(username=username).first()
        elif email:
            return Profile.objects.filter(email=email).first()
        else:
            raise GraphQLError(
                'either email or username is required to get one user.')
