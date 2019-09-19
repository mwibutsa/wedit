from wedit.apps.profiles import schema
from ..base_config import BaseGraphQLTestCase
from wedit.tests.test_fixitures.profile_fixtures import (
    query_get_profiles,
    create_profile_mutation,
    query_get_user_profile,
)
from wedit.tests.factories import ProfileFactory
from faker import Faker

fake = Faker()


class MyProfileTestCase(BaseGraphQLTestCase):

    def setUp(self):
        super(MyProfileTestCase, self).setUp()
        self.user = ProfileFactory()

    def test_query_profiles(self):
        response = self.query_with_token(
            self.admin_access_token, query_get_profiles)
        self.assertLess(0, len(response['data']['users']))

    def test_query_profile_error(self):
        response = self.query(
            '''
            query {
                user (errors: "Error") {
                    email
                }
            }
             '''
        )

    def test_create_profile_mutation(self):
        email = fake.email()
        username = fake.first_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        password = fake.password()
        response = self.query_with_token(
            self.admin_access_token,
            create_profile_mutation.format(
                email,
                username,
                first_name,
                last_name,
                password)
        )

        self.assertEqual(email, response['data']['createUser']['email'])

    def test_get_user_profile(self):
        response = self.query_with_token(
            self.user_access_token,
            query_get_user_profile.format(self.user.email)
        )
        self.assertIn('user', response['data']['user']['username'])
