# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.aave_borrow_call_data import AaveBorrowCallData

class TestAaveBorrowCallData(unittest.TestCase):
    """AaveBorrowCallData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AaveBorrowCallData:
        """Test AaveBorrowCallData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AaveBorrowCallData`
        """
        model = AaveBorrowCallData()
        if include_optional:
            return AaveBorrowCallData(
                asset = '1INCH',
                amount = None,
                interest_rate_mode = 1,
                on_behalf_of = ''
            )
        else:
            return AaveBorrowCallData(
                asset = '1INCH',
                amount = None,
                interest_rate_mode = 1,
        )
        """

    def testAaveBorrowCallData(self):
        """Test AaveBorrowCallData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
