from django.test import TestCase, Client
from wedit.apps.profiles import models
from wedit.apps.profiles import schema
from wedit.schema import schema
import json
from graphene_django.utils.testing import GraphQLTestCase


class MyProfileTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_query_profile(self):
        response = self.query(
            '''
            query {
                users {
                    email
                    password
                }
            }
            '''
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
