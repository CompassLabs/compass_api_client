# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.get_erc20_allowance_request import GetErc20AllowanceRequest

class TestGetErc20AllowanceRequest(unittest.TestCase):
    """GetErc20AllowanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetErc20AllowanceRequest:
        """Test GetErc20AllowanceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetErc20AllowanceRequest`
        """
        model = GetErc20AllowanceRequest()
        if include_optional:
            return GetErc20AllowanceRequest(
                chain = 'base:mainnet',
                user = '',
                token = '1INCH',
                contract_name = 'AaveV3Pool'
            )
        else:
            return GetErc20AllowanceRequest(
                chain = 'base:mainnet',
                user = '',
                token = '1INCH',
                contract_name = 'AaveV3Pool',
        )
        """

    def testGetErc20AllowanceRequest(self):
        """Test GetErc20AllowanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
