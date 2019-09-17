from django.test import TestCase, Client
from wedit.apps.profiles import models
from wedit.apps.profiles import schema
from wedit.schema import schema
import json
from graphene_django.utils.testing import GraphQLTestCase


class MyProfileTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def test_query_profiles(self):
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

    def test_query_user_profile(self):
        response = self.query(
            '''
            query {
                user (email: "email@gmail.com") {
                    email
                }
            }
            '''
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)

    def test_query_profile_error(self):
        response = self.query(
            '''
            query {
                user (erros: "Errro") {
                    email
                }
            }
             '''
        )

        self.assertResponseHasErrors(response)
