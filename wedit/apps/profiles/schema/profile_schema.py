from wedit.apps.profiles.models import Profile
import graphene
from graphene_django import DjangoObjectType


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
