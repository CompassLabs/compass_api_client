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

from compass.api_client.models.compass_api_backend_models_uniswap_response_lp_positions_info import CompassApiBackendModelsUniswapResponseLPPositionsInfo

class TestCompassApiBackendModelsUniswapResponseLPPositionsInfo(unittest.TestCase):
    """CompassApiBackendModelsUniswapResponseLPPositionsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompassApiBackendModelsUniswapResponseLPPositionsInfo:
        """Test CompassApiBackendModelsUniswapResponseLPPositionsInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompassApiBackendModelsUniswapResponseLPPositionsInfo`
        """
        model = CompassApiBackendModelsUniswapResponseLPPositionsInfo()
        if include_optional:
            return CompassApiBackendModelsUniswapResponseLPPositionsInfo(
                positions = {
                    'key' : compass.api_client.models.position.Position(
                        nonce = 56, 
                        operator = '', 
                        token0 = '1INCH', 
                        token1 = '1INCH', 
                        fee = '0.01', 
                        tick_lower = 56, 
                        tick_upper = 56, 
                        liquidity = 56, 
                        fee_growth_inside0_last_x128 = 56, 
                        fee_growth_inside1_last_x128 = 56, 
                        tokens_owed0 = 56, 
                        tokens_owed1 = 56, 
                        token_id = 56, )
                    }
            )
        else:
            return CompassApiBackendModelsUniswapResponseLPPositionsInfo(
                positions = {
                    'key' : compass.api_client.models.position.Position(
                        nonce = 56, 
                        operator = '', 
                        token0 = '1INCH', 
                        token1 = '1INCH', 
                        fee = '0.01', 
                        tick_lower = 56, 
                        tick_upper = 56, 
                        liquidity = 56, 
                        fee_growth_inside0_last_x128 = 56, 
                        fee_growth_inside1_last_x128 = 56, 
                        tokens_owed0 = 56, 
                        tokens_owed1 = 56, 
                        token_id = 56, )
                    },
        )
        """

    def testCompassApiBackendModelsUniswapResponseLPPositionsInfo(self):
        """Test CompassApiBackendModelsUniswapResponseLPPositionsInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
