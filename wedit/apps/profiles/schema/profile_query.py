from wedit.apps.profiles.schema.profile_schema import ProfileType
import graphene
from wedit.apps.profiles.models import Profile
from graphql_jwt.decorators import login_required, staff_member_required


class Query(graphene.ObjectType):
    users = graphene.List(ProfileType)
    user = graphene.Field(
        ProfileType, username=graphene.String(), email=graphene.String())

    @staff_member_required
    def resolve_users(self, info, **kwargs):
        return Profile.objects.all()

    @login_required
    def resolve_user(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        field, value = ('email', email) if email else (
            'username', username)
        kwargs = {f"{field}": value}
        return Profile.objects.filter(**kwargs).first()
