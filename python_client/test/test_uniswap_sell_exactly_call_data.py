# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.uniswap_sell_exactly_call_data import UniswapSellExactlyCallData

class TestUniswapSellExactlyCallData(unittest.TestCase):
    """UniswapSellExactlyCallData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UniswapSellExactlyCallData:
        """Test UniswapSellExactlyCallData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UniswapSellExactlyCallData`
        """
        model = UniswapSellExactlyCallData()
        if include_optional:
            return UniswapSellExactlyCallData(
                token_in = '1INCH',
                token_out = '1INCH',
                fee = '0.01',
                amount_in = None,
                amount_out_minimum = None,
                wrap_eth = True
            )
        else:
            return UniswapSellExactlyCallData(
                token_in = '1INCH',
                token_out = '1INCH',
                fee = '0.01',
                amount_in = None,
        )
        """

    def testUniswapSellExactlyCallData(self):
        """Test UniswapSellExactlyCallData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
