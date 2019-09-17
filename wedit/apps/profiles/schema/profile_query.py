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
        field, value = ('email', email) if email else (
            'username', username)
        kwargs = {f"{field}": value}
        return Profile.objects.filter(**kwargs).first()
