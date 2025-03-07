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

from compass.api_client.models.aerodrome_swap_tokens_call_data import AerodromeSwapTokensCallData

class TestAerodromeSwapTokensCallData(unittest.TestCase):
    """AerodromeSwapTokensCallData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AerodromeSwapTokensCallData:
        """Test AerodromeSwapTokensCallData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AerodromeSwapTokensCallData`
        """
        model = AerodromeSwapTokensCallData()
        if include_optional:
            return AerodromeSwapTokensCallData(
                token_in = '1INCH',
                token_out = '1INCH',
                amount_in = None,
                amount_out_min = None,
                stable = True,
                to = ''
            )
        else:
            return AerodromeSwapTokensCallData(
                token_in = '1INCH',
                token_out = '1INCH',
                amount_in = None,
                amount_out_min = None,
                stable = True,
        )
        """

    def testAerodromeSwapTokensCallData(self):
        """Test AerodromeSwapTokensCallData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
