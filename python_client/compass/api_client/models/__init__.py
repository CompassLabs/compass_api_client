# coding: utf-8

# flake8: noqa
"""
    Compass API

      <h3>With this API you can:</h3> <ul> <li><strong>Execute complex DeFi transactions:&nbsp; </strong>Swap, lend, borrow, stake, LP, and more, with high-level on-chain actions.</li> <li><strong>Stay secure &amp; non-custodial</strong> &ndash; Transactions are signed locally, and you retain full control.</li> <li><strong>Build AI &amp; automation workflows</strong> &ndash; Power AI agents, trading bots, yield products and DeFi applications with programmatic transaction execution. Integrate seamlessly into existing workflows.</li> <li><strong>Interact across multiple protocols &amp; chains</strong>&nbsp;&ndash; Spot, lending, staking on Ethereum, Arbitrum, Base. Many more to come!</li> </ul>  <h3 id=\"quick-links\" class=\"docs-chapter-header\"><a class=\"not-prose group hover:text-compass-pink transition-colors flex w-fit\" href=\"https://www.compasslabs.ai/api-docs#quick-links\">Quick links</a></h3> <ul> <li><a href=\"https://api.compasslabs.ai/\" target=\"_blank\" rel=\"noopener\">API reference</a></li> <li><a href=\"https://github.com/CompassLabs/compass_api_examples\" target=\"_blank\" rel=\"noopener\">5 min quickstart</a></li> <li><a href=\"https://discord.gg/qjP8dCYZ58\" target=\"_blank\" rel=\"noopener\">Discord</a></li> <li><a href=\"https://www.compasslabs.ai/\" target=\"_blank\" rel=\"noopener\">Compass Labs</a></li> </ul>

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from compass.api_client.models.aave_asset_price_info import AaveAssetPriceInfo
from compass.api_client.models.aave_borrow_call_data import AaveBorrowCallData
from compass.api_client.models.aave_get_asset_price import AaveGetAssetPrice
from compass.api_client.models.aave_get_liquidity_change import AaveGetLiquidityChange
from compass.api_client.models.aave_get_user_position_per_token import AaveGetUserPositionPerToken
from compass.api_client.models.aave_get_user_position_summary import AaveGetUserPositionSummary
from compass.api_client.models.aave_liquidity_change import AaveLiquidityChange
from compass.api_client.models.aave_repay_call_data import AaveRepayCallData
from compass.api_client.models.aave_supply_call_data import AaveSupplyCallData
from compass.api_client.models.aave_user_position_per_token_info import AaveUserPositionPerTokenInfo
from compass.api_client.models.aave_user_position_summary_info import AaveUserPositionSummaryInfo
from compass.api_client.models.aave_withdraw_call_data import AaveWithdrawCallData
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
from compass.api_client.models.allowance_info import AllowanceInfo
from compass.api_client.models.amount import Amount
from compass.api_client.models.amount0_desired import Amount0Desired
from compass.api_client.models.amount0_min import Amount0Min
from compass.api_client.models.amount1 import Amount1
from compass.api_client.models.amount1_desired import Amount1Desired
from compass.api_client.models.amount1_min import Amount1Min
from compass.api_client.models.amount2 import Amount2
from compass.api_client.models.amount3 import Amount3
from compass.api_client.models.amount4 import Amount4
from compass.api_client.models.amount5 import Amount5
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
from compass.api_client.models.balance_info import BalanceInfo
from compass.api_client.models.base_transaction_request_aave_borrow_call_data import BaseTransactionRequestAaveBorrowCallData
from compass.api_client.models.base_transaction_request_aave_repay_call_data import BaseTransactionRequestAaveRepayCallData
from compass.api_client.models.base_transaction_request_aave_supply_call_data import BaseTransactionRequestAaveSupplyCallData
from compass.api_client.models.base_transaction_request_aave_withdraw_call_data import BaseTransactionRequestAaveWithdrawCallData
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
from compass.api_client.models.base_transaction_request_increase_erc20_allowance_any_call_data import BaseTransactionRequestIncreaseErc20AllowanceAnyCallData
from compass.api_client.models.base_transaction_request_increase_erc20_allowance_call_data import BaseTransactionRequestIncreaseErc20AllowanceCallData
from compass.api_client.models.base_transaction_request_uniswap_buy_exactly_call_data import BaseTransactionRequestUniswapBuyExactlyCallData
from compass.api_client.models.base_transaction_request_uniswap_increase_liquidity_provision_call_data import BaseTransactionRequestUniswapIncreaseLiquidityProvisionCallData
from compass.api_client.models.base_transaction_request_uniswap_mint_liquidity_provision_call_data import BaseTransactionRequestUniswapMintLiquidityProvisionCallData
from compass.api_client.models.base_transaction_request_uniswap_sell_exactly_call_data import BaseTransactionRequestUniswapSellExactlyCallData
from compass.api_client.models.base_transaction_request_uniswap_withdraw_liquidity_provision_call_data import BaseTransactionRequestUniswapWithdrawLiquidityProvisionCallData
from compass.api_client.models.base_transaction_request_unwrap_weth_request_call_data import BaseTransactionRequestUnwrapWethRequestCallData
from compass.api_client.models.base_transaction_request_wrap_eth_request_call_data import BaseTransactionRequestWrapEthRequestCallData
from compass.api_client.models.chain import Chain
from compass.api_client.models.contract_name import ContractName
from compass.api_client.models.ens_name_info import EnsNameInfo
from compass.api_client.models.fee_enum import FeeEnum
from compass.api_client.models.get_erc20_allowance import GetErc20Allowance
from compass.api_client.models.get_erc20_balance import GetErc20Balance
from compass.api_client.models.get_supported_tokens import GetSupportedTokens
from compass.api_client.models.http_validation_error import HTTPValidationError
from compass.api_client.models.image import Image
from compass.api_client.models.increase_erc20_allowance_any_call_data import IncreaseErc20AllowanceAnyCallData
from compass.api_client.models.increase_erc20_allowance_call_data import IncreaseErc20AllowanceCallData
from compass.api_client.models.interest_rate_mode import InterestRateMode
from compass.api_client.models.liquidity import Liquidity
from compass.api_client.models.percentage_for_withdrawal import PercentageForWithdrawal
from compass.api_client.models.portfolio import Portfolio
from compass.api_client.models.request_ens_details import RequestEnsDetails
from compass.api_client.models.request_user_address import RequestUserAddress
from compass.api_client.models.token import Token
from compass.api_client.models.token0_token1 import Token0Token1
from compass.api_client.models.token_balance import TokenBalance
from compass.api_client.models.token_info import TokenInfo
from compass.api_client.models.uniswap_buy_exactly_call_data import UniswapBuyExactlyCallData
from compass.api_client.models.uniswap_buy_quote_info import UniswapBuyQuoteInfo
from compass.api_client.models.uniswap_check_in_range_call_data import UniswapCheckInRangeCallData
from compass.api_client.models.uniswap_check_in_range_response import UniswapCheckInRangeResponse
from compass.api_client.models.uniswap_get_buy_quote import UniswapGetBuyQuote
from compass.api_client.models.uniswap_get_liquidity_provision_positions import UniswapGetLiquidityProvisionPositions
from compass.api_client.models.uniswap_get_pool_price import UniswapGetPoolPrice
from compass.api_client.models.uniswap_get_sell_quote import UniswapGetSellQuote
from compass.api_client.models.uniswap_impermanent_loss_call_data import UniswapImpermanentLossCallData
from compass.api_client.models.uniswap_impermanent_loss_response import UniswapImpermanentLossResponse
from compass.api_client.models.uniswap_increase_liquidity_provision_call_data import UniswapIncreaseLiquidityProvisionCallData
from compass.api_client.models.uniswap_lp_positions_info import UniswapLPPositionsInfo
from compass.api_client.models.uniswap_mint_liquidity_provision_call_data import UniswapMintLiquidityProvisionCallData
from compass.api_client.models.uniswap_pool_price import UniswapPoolPrice
from compass.api_client.models.uniswap_position import UniswapPosition
from compass.api_client.models.uniswap_sell_exactly_call_data import UniswapSellExactlyCallData
from compass.api_client.models.uniswap_sell_quote_info import UniswapSellQuoteInfo
from compass.api_client.models.uniswap_withdraw_liquidity_provision_call_data import UniswapWithdrawLiquidityProvisionCallData
from compass.api_client.models.unsigned_transaction import UnsignedTransaction
from compass.api_client.models.unwrap_weth_request_call_data import UnwrapWethRequestCallData
from compass.api_client.models.validation_error import ValidationError
from compass.api_client.models.validation_error_loc_inner import ValidationErrorLocInner
from compass.api_client.models.wrap_eth_request_call_data import WrapEthRequestCallData
