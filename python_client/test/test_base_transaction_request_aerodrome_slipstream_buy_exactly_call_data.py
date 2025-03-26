# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.base_transaction_request_aerodrome_slipstream_buy_exactly_call_data import BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData

class TestBaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData(unittest.TestCase):
    """BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData:
        """Test BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData`
        """
        model = BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData()
        if include_optional:
            return BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData(
                chain = 'base:mainnet',
                sender = '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                call_data = compass.api_client.models.aerodrome_slipstream_buy_exactly_call_data.AerodromeSlipstreamBuyExactlyCallData(
                    token_in = '1INCH', 
                    token_out = '1INCH', 
                    tick_spacing = 1.0, 
                    amount_out = null, 
                    amount_in_maximum = null, )
            )
        else:
            return BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData(
                chain = 'base:mainnet',
                sender = '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                call_data = compass.api_client.models.aerodrome_slipstream_buy_exactly_call_data.AerodromeSlipstreamBuyExactlyCallData(
                    token_in = '1INCH', 
                    token_out = '1INCH', 
                    tick_spacing = 1.0, 
                    amount_out = null, 
                    amount_in_maximum = null, ),
        )
        """

    def testBaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData(self):
        """Test BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
