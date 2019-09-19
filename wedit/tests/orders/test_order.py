from wedit.tests.base_config import BaseGraphQLTestCase
from wedit.tests.test_fixitures.order_fixitures import order_mutation
from faker import Faker
import re
fake = Faker()


class OrderTest(BaseGraphQLTestCase):

    def setUp(self):
        super(OrderTest, self).setUp()

    def test_create_design_order(self):
        orderTitle = "fake title"
        orderFile = "fake/file/name.txt"
        orderSummary = "fake summary"
        descriptionFile = "fake/file.img"

        response = self.query_with_token(self.user_access_token, order_mutation.format(
            orderTitle, orderFile, orderSummary, descriptionFile
        ))
        self.assertIn(
            'fake', response['data']['createOrder']['orderTitle'])
