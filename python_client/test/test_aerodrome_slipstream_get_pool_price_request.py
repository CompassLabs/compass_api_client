# coding: utf-8

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from compass.api_client.models.aerodrome_slipstream_get_pool_price_request import AerodromeSlipstreamGetPoolPriceRequest

class TestAerodromeSlipstreamGetPoolPriceRequest(unittest.TestCase):
    """AerodromeSlipstreamGetPoolPriceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AerodromeSlipstreamGetPoolPriceRequest:
        """Test AerodromeSlipstreamGetPoolPriceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AerodromeSlipstreamGetPoolPriceRequest`
        """
        model = AerodromeSlipstreamGetPoolPriceRequest()
        if include_optional:
            return AerodromeSlipstreamGetPoolPriceRequest(
                chain = 'base:mainnet',
                token_in = '1INCH',
                token_out = '1INCH',
                tick_spacing = 1.0
            )
        else:
            return AerodromeSlipstreamGetPoolPriceRequest(
                chain = 'base:mainnet',
                token_in = '1INCH',
                token_out = '1INCH',
                tick_spacing = 1.0,
        )
        """

    def testAerodromeSlipstreamGetPoolPriceRequest(self):
        """Test AerodromeSlipstreamGetPoolPriceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
