from wedit.apps.profiles.models import Profile
from graphene_django import DjangoObjectType


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
