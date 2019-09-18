import factory
from wedit.apps.profiles.models import Profile
from wedit.apps.orders.models import Order
from faker import Faker

fake = Faker()


class ProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = Profile

    email = factory.Sequence(lambda x: "user%d@gmail.com" % x)
    username = factory.Sequence(lambda x: "user%x" % x)
    first_name = fake.first_name()
    last_name = fake.last_name()
    active = True
    admin = False
    staff = False
    editor = False
    password = factory.PostGenerationMethodCall(
        'set_password', 'Password@1')


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = Order

    owner = factory.SubFactory(ProfileFactory)

    orderTitle = fake.sentence()
    orderFile = fake.sentence()
    orderSummary = fake.text()
    descriptionFile = fake.text()
