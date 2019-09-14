import json
from django.test import TestCase
from django.test import Client


class BaseGraphQLTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.content_type = 'application/json'
        self.url = '/wedit/'

    def query_with_token(self, access_token, query: str):
        body = dict()
        body['query'] = query

        http_auth = 'JWT {}'.format(access_token)
        url = '/wedit/'
        content_type = 'application/json'
        response = self.client.post(
            url,
            json.dumps(
                body),
            HTTP_AUTHORIZATION=http_auth,
            content_type=content_type)

        json_response = json.loads(response.content.decode())
        return json_response

    def query(self, query: str):

        body = dict()
        body['query'] = query

        response = self.client.post(
            self.url,
            json.dumps(body),
            content_type=self.content_type
        )

        json_response = json.loads(response.content.decode())
        return json_response
