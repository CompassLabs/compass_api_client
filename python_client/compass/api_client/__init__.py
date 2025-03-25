# coding: utf-8

# flake8: noqa

"""
    Compass API

    #### Welcome to the DeFi API from [Compass Labs](https://www.compasslabs.ai)!  Our API allows you to interact and transact in DeFi with ease.  We help you construct your transactions via a **simple REST API**.   You maintain custody at all times and **sign** all transactions **yourself**.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.107"

# import apis into sdk package
from compass.api_client.api.aave_v3_api import AaveV3Api
from compass.api_client.api.aerodrome_basic_api import AerodromeBasicApi
from compass.api_client.api.aerodrome_slipstream_api import AerodromeSlipstreamApi
from compass.api_client.api.others_api import OthersApi
from compass.api_client.api.uniswap_v3_api import UniswapV3Api

# import ApiClient
from compass.api_client.api_response import ApiResponse
from compass.api_client.api_client import ApiClient
from compass.api_client.configuration import Configuration
from compass.api_client.exceptions import OpenApiException
from compass.api_client.exceptions import ApiTypeError
from compass.api_client.exceptions import ApiValueError
from compass.api_client.exceptions import ApiKeyError
from compass.api_client.exceptions import ApiAttributeError
from compass.api_client.exceptions import ApiException

# import models into sdk package
from compass.api_client.models.aave_asset_price_response import AaveAssetPriceResponse
from compass.api_client.models.aave_borrow_request import AaveBorrowRequest
from compass.api_client.models.aave_get_asset_price_request import AaveGetAssetPriceRequest
from compass.api_client.models.aave_get_liquidity_change_request import AaveGetLiquidityChangeRequest
from compass.api_client.models.aave_get_user_position_per_token_request import AaveGetUserPositionPerTokenRequest
from compass.api_client.models.aave_get_user_position_summary_request import AaveGetUserPositionSummaryRequest
from compass.api_client.models.aave_liquidity_change_response import AaveLiquidityChangeResponse
from compass.api_client.models.aave_repay_request import AaveRepayRequest
from compass.api_client.models.aave_supply_request import AaveSupplyRequest
from compass.api_client.models.aave_user_position_per_token_response import AaveUserPositionPerTokenResponse
from compass.api_client.models.aave_user_position_summary_response import AaveUserPositionSummaryResponse
from compass.api_client.models.aave_withdraw_request import AaveWithdrawRequest
from compass.api_client.models.aerodrome_lp_positions_info import AerodromeLPPositionsInfo
from compass.api_client.models.aerodrome_liquidity_provision_call_data import AerodromeLiquidityProvisionCallData
from compass.api_client.models.aerodrome_liquidity_provision_eth_call_data import AerodromeLiquidityProvisionEthCallData
from compass.api_client.models.aerodrome_position import AerodromePosition
from compass.api_client.models.aerodrome_remove_liquidity_call_data import AerodromeRemoveLiquidityCallData
from compass.api_client.models.aerodrome_remove_liquidity_eth_call_data import AerodromeRemoveLiquidityEthCallData
from compass.api_client.models.aerodrome_slipstream_buy_exactly_call_data import AerodromeSlipstreamBuyExactlyCallData
from compass.api_client.models.aerodrome_slipstream_get_liquidity_provision_positions import AerodromeSlipstreamGetLiquidityProvisionPositions
from compass.api_client.models.aerodrome_slipstream_get_pool_price import AerodromeSlipstreamGetPoolPrice
from compass.api_client.models.aerodrome_slipstream_increase_liquidity_provision_call_data import AerodromeSlipstreamIncreaseLiquidityProvisionCallData
from compass.api_client.models.aerodrome_slipstream_mint_liquidity_provision_call_data import AerodromeSlipstreamMintLiquidityProvisionCallData
from compass.api_client.models.aerodrome_slipstream_pool_price import AerodromeSlipstreamPoolPrice
from compass.api_client.models.aerodrome_slipstream_sell_exactly_call_data import AerodromeSlipstreamSellExactlyCallData
from compass.api_client.models.aerodrome_slipstream_withdraw_liquidity_provision_call_data import AerodromeSlipstreamWithdrawLiquidityProvisionCallData
from compass.api_client.models.aerodrome_swap_eth_for_token_call_data import AerodromeSwapEthForTokenCallData
from compass.api_client.models.aerodrome_swap_token_for_eth_call_data import AerodromeSwapTokenForEthCallData
from compass.api_client.models.aerodrome_swap_tokens_call_data import AerodromeSwapTokensCallData
from compass.api_client.models.allowance_info_response import AllowanceInfoResponse
from compass.api_client.models.amount import Amount
from compass.api_client.models.amount0_desired import Amount0Desired
from compass.api_client.models.amount0_desired1 import Amount0Desired1
from compass.api_client.models.amount0_min import Amount0Min
from compass.api_client.models.amount0_min1 import Amount0Min1
from compass.api_client.models.amount1 import Amount1
from compass.api_client.models.amount1_desired import Amount1Desired
from compass.api_client.models.amount1_desired1 import Amount1Desired1
from compass.api_client.models.amount1_min import Amount1Min
from compass.api_client.models.amount1_min1 import Amount1Min1
from compass.api_client.models.amount2 import Amount2
from compass.api_client.models.amount3 import Amount3
from compass.api_client.models.amount4 import Amount4
from compass.api_client.models.amount5 import Amount5
from compass.api_client.models.amount6 import Amount6
from compass.api_client.models.amount7 import Amount7
from compass.api_client.models.amount8 import Amount8
from compass.api_client.models.amount_a_desired import AmountADesired
from compass.api_client.models.amount_a_min import AmountAMin
from compass.api_client.models.amount_a_min1 import AmountAMin1
from compass.api_client.models.amount_b_desired import AmountBDesired
from compass.api_client.models.amount_b_min import AmountBMin
from compass.api_client.models.amount_b_min1 import AmountBMin1
from compass.api_client.models.amount_eth_desired import AmountEthDesired
from compass.api_client.models.amount_eth_min import AmountEthMin
from compass.api_client.models.amount_eth_min1 import AmountEthMin1
from compass.api_client.models.amount_in import AmountIn
from compass.api_client.models.amount_in1 import AmountIn1
from compass.api_client.models.amount_in2 import AmountIn2
from compass.api_client.models.amount_in_maximum import AmountInMaximum
from compass.api_client.models.amount_out import AmountOut
from compass.api_client.models.amount_out_min import AmountOutMin
from compass.api_client.models.amount_out_min1 import AmountOutMin1
from compass.api_client.models.amount_out_minimum import AmountOutMinimum
from compass.api_client.models.amount_token_desired import AmountTokenDesired
from compass.api_client.models.amount_token_min import AmountTokenMin
from compass.api_client.models.amount_token_min1 import AmountTokenMin1
from compass.api_client.models.balance_info_response import BalanceInfoResponse
from compass.api_client.models.base_transaction_request_aerodrome_liquidity_provision_call_data import BaseTransactionRequestAerodromeLiquidityProvisionCallData
from compass.api_client.models.base_transaction_request_aerodrome_liquidity_provision_eth_call_data import BaseTransactionRequestAerodromeLiquidityProvisionEthCallData
from compass.api_client.models.base_transaction_request_aerodrome_remove_liquidity_call_data import BaseTransactionRequestAerodromeRemoveLiquidityCallData
from compass.api_client.models.base_transaction_request_aerodrome_remove_liquidity_eth_call_data import BaseTransactionRequestAerodromeRemoveLiquidityEthCallData
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_buy_exactly_call_data import BaseTransactionRequestAerodromeSlipstreamBuyExactlyCallData
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_increase_liquidity_provision_call_data import BaseTransactionRequestAerodromeSlipstreamIncreaseLiquidityProvisionCallData
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_mint_liquidity_provision_call_data import BaseTransactionRequestAerodromeSlipstreamMintLiquidityProvisionCallData
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_sell_exactly_call_data import BaseTransactionRequestAerodromeSlipstreamSellExactlyCallData
from compass.api_client.models.base_transaction_request_aerodrome_slipstream_withdraw_liquidity_provision_call_data import BaseTransactionRequestAerodromeSlipstreamWithdrawLiquidityProvisionCallData
from compass.api_client.models.base_transaction_request_aerodrome_swap_eth_for_token_call_data import BaseTransactionRequestAerodromeSwapEthForTokenCallData
from compass.api_client.models.base_transaction_request_aerodrome_swap_token_for_eth_call_data import BaseTransactionRequestAerodromeSwapTokenForEthCallData
from compass.api_client.models.base_transaction_request_aerodrome_swap_tokens_call_data import BaseTransactionRequestAerodromeSwapTokensCallData
from compass.api_client.models.chain import Chain
from compass.api_client.models.contract_name import ContractName
from compass.api_client.models.ens_name_info_response import EnsNameInfoResponse
from compass.api_client.models.fee_enum import FeeEnum
from compass.api_client.models.get_ens_details_request import GetEnsDetailsRequest
from compass.api_client.models.get_erc20_allowance_request import GetErc20AllowanceRequest
from compass.api_client.models.get_erc20_balance_request import GetErc20BalanceRequest
from compass.api_client.models.http_validation_error import HTTPValidationError
from compass.api_client.models.image import Image
from compass.api_client.models.increase_allowance_any_request import IncreaseAllowanceAnyRequest
from compass.api_client.models.increase_allowance_request import IncreaseAllowanceRequest
from compass.api_client.models.interest_rate_mode import InterestRateMode
from compass.api_client.models.liquidity import Liquidity
from compass.api_client.models.percentage_for_withdrawal import PercentageForWithdrawal
from compass.api_client.models.portfolio import Portfolio
from compass.api_client.models.portfolio_request import PortfolioRequest
from compass.api_client.models.price_request import PriceRequest
from compass.api_client.models.price_response import PriceResponse
from compass.api_client.models.token import Token
from compass.api_client.models.token_balance import TokenBalance
from compass.api_client.models.token_info import TokenInfo
from compass.api_client.models.tokens_request import TokensRequest
from compass.api_client.models.transfer_erc20_request import TransferERC20Request
from compass.api_client.models.transfer_eth_request import TransferEthRequest
from compass.api_client.models.uniswap_buy_exactly_request import UniswapBuyExactlyRequest
from compass.api_client.models.uniswap_buy_quote_info_response import UniswapBuyQuoteInfoResponse
from compass.api_client.models.uniswap_check_in_range_request import UniswapCheckInRangeRequest
from compass.api_client.models.uniswap_check_in_range_response import UniswapCheckInRangeResponse
from compass.api_client.models.uniswap_get_buy_quote_request import UniswapGetBuyQuoteRequest
from compass.api_client.models.uniswap_get_liquidity_provision_positions_request import UniswapGetLiquidityProvisionPositionsRequest
from compass.api_client.models.uniswap_get_pool_price_request import UniswapGetPoolPriceRequest
from compass.api_client.models.uniswap_get_sell_quote_request import UniswapGetSellQuoteRequest
from compass.api_client.models.uniswap_increase_liquidity_provision import UniswapIncreaseLiquidityProvision
from compass.api_client.models.uniswap_lp_positions_info_response import UniswapLPPositionsInfoResponse
from compass.api_client.models.uniswap_mint_liquidity_provision import UniswapMintLiquidityProvision
from compass.api_client.models.uniswap_pool_price_response import UniswapPoolPriceResponse
from compass.api_client.models.uniswap_position import UniswapPosition
from compass.api_client.models.uniswap_sell_exactly_request import UniswapSellExactlyRequest
from compass.api_client.models.uniswap_sell_quote_info_response import UniswapSellQuoteInfoResponse
from compass.api_client.models.uniswap_withdraw_liquidity_provision import UniswapWithdrawLiquidityProvision
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.models.unwrap_weth_request import UnwrapWethRequest
from compass.api_client.models.validation_error import ValidationError
from compass.api_client.models.validation_error_loc_inner import ValidationErrorLocInner
from compass.api_client.models.visualize_portfolio_request import VisualizePortfolioRequest
from compass.api_client.models.wrap_eth_request import WrapEthRequest
