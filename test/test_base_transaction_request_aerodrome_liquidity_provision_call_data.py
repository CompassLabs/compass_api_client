# coding: utf-8

"""
    Compass API

      #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.  Below is the documentation of our endpoints. It's a great first step to explore.  

    The version of the OpenAPI document: 0.0.1
    Contact: contact@compasslabs.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.base_transaction_request_aerodrome_liquidity_provision_call_data import BaseTransactionRequestAerodromeLiquidityProvisionCallData

class TestBaseTransactionRequestAerodromeLiquidityProvisionCallData(unittest.TestCase):
    """BaseTransactionRequestAerodromeLiquidityProvisionCallData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseTransactionRequestAerodromeLiquidityProvisionCallData:
        """Test BaseTransactionRequestAerodromeLiquidityProvisionCallData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseTransactionRequestAerodromeLiquidityProvisionCallData`
        """
        model = BaseTransactionRequestAerodromeLiquidityProvisionCallData()
        if include_optional:
            return BaseTransactionRequestAerodromeLiquidityProvisionCallData(
                chain = 'ethereum:mainnet',
                sender = '',
                call_data = compass.api_client.models.aerodrome_liquidity_provision_call_data.AerodromeLiquidityProvisionCallData(
                    token_a = '1INCH', 
                    token_b = '1INCH', 
                    stable = True, 
                    amount_a_desired = null, 
                    amount_b_desired = null, 
                    amount_a_min = null, 
                    amount_b_min = null, 
                    to = '', 
                    deadline = 56, )
            )
        else:
            return BaseTransactionRequestAerodromeLiquidityProvisionCallData(
                chain = 'ethereum:mainnet',
                sender = '',
                call_data = compass.api_client.models.aerodrome_liquidity_provision_call_data.AerodromeLiquidityProvisionCallData(
                    token_a = '1INCH', 
                    token_b = '1INCH', 
                    stable = True, 
                    amount_a_desired = null, 
                    amount_b_desired = null, 
                    amount_a_min = null, 
                    amount_b_min = null, 
                    to = '', 
                    deadline = 56, ),
        )
        """

    def testBaseTransactionRequestAerodromeLiquidityProvisionCallData(self):
        """Test BaseTransactionRequestAerodromeLiquidityProvisionCallData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
