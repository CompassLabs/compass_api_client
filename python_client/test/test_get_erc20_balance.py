# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.get_erc20_balance import GetErc20Balance

class TestGetErc20Balance(unittest.TestCase):
    """GetErc20Balance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetErc20Balance:
        """Test GetErc20Balance
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetErc20Balance`
        """
        model = GetErc20Balance()
        if include_optional:
            return GetErc20Balance(
                chain = 'ethereum:mainnet',
                user = '',
                token = '1INCH'
            )
        else:
            return GetErc20Balance(
                chain = 'ethereum:mainnet',
                user = '',
                token = '1INCH',
        )
        """

    def testGetErc20Balance(self):
        """Test GetErc20Balance"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
