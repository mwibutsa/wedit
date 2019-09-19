import graphene
from wedit.apps.profiles.models import Profile


class CreateUser(graphene.Mutation):
    email = graphene.String()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    password = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        password = graphene.String(required=True)

    def mutate(self, info, email, username, password, first_name, last_name):
        profile = Profile(email=email, username=username,
                          first_name=first_name, last_name=last_name)
        profile.set_password(password)
        profile.save()
        return CreateUser(
            email=profile.email,
            username=profile.username,
            first_name=profile.first_name,
            last_name=profile.last_name,
            password=profile.password
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
