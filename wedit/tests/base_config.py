import json
from django.test import TestCase
from django.test import Client
from wedit.apps.profiles.models import Profile
from wedit.apps.orders.models import Order
from wedit.tests.factories import ProfileFactory, OrderFactory
from wedit.tests.test_fixitures.profile_fixtures import user_login_mutation


class BaseGraphQLTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.content_type = 'application/json'
        self.url = '/graphql/'
        self.user_access_token = self.login_user()
        self.admin_access_token = self.login_admin()
        self.editor_access_token = self.login_editor()

    def query_with_token(self, access_token, query: str):
        body = dict()
        body['query'] = query

        http_auth = 'JWT {}'.format(access_token)
        content_type = 'application/json'
        response = self.client.post(
            self.url,
            json.dumps(
                body),
            HTTP_AUTHORIZATION=http_auth,
            content_type=content_type)

        content = response.content
        json_response = json.loads(content.decode())
        return json_response

    def query(self, query: str):

        body = dict()
        body['query'] = query

        response = self.client.post(
            self.url,
            json.dumps(body),
            content_type=self.content_type
        )

        content = response.content
        json_response = json.loads(content.decode())
        return json_response

    def register_user(self):
        return ProfileFactory()

    def register_admin(self):
        return ProfileFactory(admin=True, staff=True)

    def register_editor(self):
        return ProfileFactory(editor=True)

    def login_admin(self):
        user = self.register_admin()
        response = self.query(
            user_login_mutation.format(user.email, 'Password@1'))
        return response['data']['login']['token']

    def login_editor(self):
        user = self.register_editor()
        response = self.query(
            user_login_mutation.format(user.email, 'Password@1'))
        return response['data']['login']['token']

    def login_user(self):
        user = self.register_user()
        response = self.query(
            user_login_mutation.format(user.email, 'Password@1'))
        return response['data']['login']['token']
