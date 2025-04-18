import { makeApi, Zodios, type ZodiosOptions } from '@zodios/core';
import { z } from 'zod';

const Token = z.enum([
    '1INCH',
    'AAVE',
    'BAL',
    'cbBTC',
    'cbETH',
    'CRV',
    'crvUSD',
    'DAI',
    'ENS',
    'ETHx',
    'FRAX',
    'FXS',
    'GHO',
    'KNC',
    'LDO',
    'LINK',
    'LUSD',
    'MKR',
    'osETH',
    'PYUSD',
    'rETH',
    'RPL',
    'rsETH',
    'sDAI',
    'SNX',
    'STG',
    'sUSDe',
    'tBTC',
    'UNI',
    'USDC',
    'USDe',
    'USDS',
    'USDT',
    'WBTC',
    'weETH',
    'WETH',
    'wstETH',
    'ARB',
    'EURS',
    'MAI',
    'USDCe',
    'AERO',
    'EUR',
    'VIRTUAL',
]);
const Chain = z.enum(['base:mainnet', 'ethereum:mainnet', 'arbitrum:mainnet']);
const AaveSupplyRequest = z
    .object({
        asset: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        amount: z.union([z.number(), z.string()]).describe('The amount of the asset to supply'),
        on_behalf_of: z
            .union([z.string(), z.null()])
            .describe(
                'The address on behalf of whom the supply is made. Defaults to the transaction sender.'
            )
            .optional()
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UnsignedTransaction = z
    .object({
        chainId: z.number().int().describe('The chain id of the transaction'),
        data: z.string().describe('The data of the transaction'),
        from: z.string().describe('The sender of the transaction'),
        gas: z.number().int().describe('The gas of the transaction'),
        to: z.string().describe('The recipient of the transaction'),
        value: z.number().int().describe('The value of the transaction'),
        nonce: z.number().int().describe('The nonce of the address'),
        maxFeePerGas: z.number().int().describe('The max fee per gas of the transaction'),
        maxPriorityFeePerGas: z
            .number()
            .int()
            .describe('The max priority fee per gas of the transaction'),
    })
    .passthrough();
const ValidationError = z
    .object({
        loc: z.array(z.union([z.string(), z.number()])),
        msg: z.string(),
        type: z.string(),
    })
    .passthrough();
const HTTPValidationError = z
    .object({ detail: z.array(ValidationError) })
    .partial()
    .passthrough();
const InterestRateMode = z.enum(['stable', 'variable']);
const AaveBorrowRequest = z
    .object({
        asset: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        amount: z.union([z.number(), z.string()]).describe('The amount of the asset to borrow'),
        interest_rate_mode: InterestRateMode.describe(`On AAVE there are 2 different interest modes.

A stable (but typically higher rate), or a variable rate.`),
        on_behalf_of: z
            .union([z.string(), z.null()])
            .describe('The address on behalf of whom the supply is made')
            .optional()
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AaveRepayRequest = z
    .object({
        asset: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        amount: z.union([z.number(), z.string()]).describe('The amount of the asset to repay'),
        interest_rate_mode: InterestRateMode.describe(`On AAVE there are 2 different interest modes.

A stable (but typically higher rate), or a variable rate.`),
        on_behalf_of: z
            .union([z.string(), z.null()])
            .describe('The address on behalf of whom the supply is made')
            .optional()
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AaveWithdrawRequest = z
    .object({
        asset: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        amount: z.union([z.number(), z.string()]).describe('The amount of the asset to withdraw'),
        recipient: z.string().describe('The address of the recipient of the withdrawn funds.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AaveGetAssetPriceRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        asset: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
    })
    .passthrough();
const AaveAssetPriceResponse = z
    .object({ price: z.string().describe('The price of the asset in USD.') })
    .passthrough();
const AaveGetLiquidityChangeRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        start_block: z.number().int().describe('The starting block.'),
        end_block: z
            .union([z.number(), z.null()])
            .describe('The ending block. If nothing provided defaults to latest')
            .optional(),
        asset: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
    })
    .passthrough();
const AaveLiquidityChangeResponse = z
    .object({
        liquidity_change: z
            .string()
            .describe(
                'The change in the liqudiity index between the two times, expressed as a percentage.'
            ),
        start_time: z.string().datetime({ offset: true }).describe('Dateime of starting block'),
        end_time: z.string().datetime({ offset: true }).describe('Dateime of ending block'),
    })
    .passthrough();
const AaveGetUserPositionSummaryRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z.string().describe('The user to get the position summary of. Values are in USD.'),
    })
    .passthrough();
const AaveUserPositionSummaryResponse = z
    .object({
        maximum_loan_to_value_ratio: z.string().describe('The loan to value ratio of a user.'),
        health_factor: z
            .string()
            .describe(`The health factor of a user. If this is above 1 it is safe; below 1 and the
        user is in risk of liquidation. This number might be very high (which would mean the user is
        safe!)`),
        total_collateral: z.string().describe('The total collateral (in USD) of a user.'),
        total_debt: z.string().describe('The total debt (in USD) of a user.'),
        available_borrows: z.string().describe('The available borrows (in USD) of a user.'),
        liquidation_threshold: z
            .string()
            .describe(`The liquidation threshold of a user. A user might exceed this due to changing
        asset values.`),
    })
    .passthrough();
const AaveGetUserPositionPerTokenRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z.string().describe('The user to fetch the token-specific position of.'),
        asset: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
    })
    .passthrough();
const AaveUserPositionPerTokenResponse = z
    .object({
        token_balance: z
            .string()
            .describe(
                'The balance of AAVE aTokens (interest-bearing representations of your deposits).'
            ),
        stable_debt: z
            .string()
            .describe("The amount of the user's debt with a fixed interest rate."),
        variable_debt: z
            .string()
            .describe("The amount of the user's debt with a variable interest rate."),
        principal_stable_debt: z
            .string()
            .describe(`The amount of the user's debt that was part of the initial principal of all
        loans with a stable interest rate.`),
        principal_variable_debt: z
            .string()
            .describe(`The amount of the user's debt that was part of the initial principal of all
        loans with a variable interest rate. This is the value stored by AAVE, which may be slightly
        inaccurate, but reflects what AAVE believes you initially paid.`),
        stable_borrow_rate: z
            .string()
            .describe(`The current average annualised interest rate for all your stable loans in
        this pool.`),
        stable_borrow_rate_for_new_loans: z
            .string()
            .describe('The annualised interest rate you would pay on a new stable loan.'),
        variable_borrow_rate: z
            .string()
            .describe(`The current annualised interest rate for variable rate loans in this pool.
        (This applies to both current and new loans.)`),
        liquidity_rate: z.string().describe('The annualised interest rate for deposited supplies.'),
    })
    .passthrough();
const AerodromeSlipstreamSellExactlyRequest = z
    .object({
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        tick_spacing: z.number().int().gte(1).describe('The tick spacing of the pool'),
        amount_in: z
            .union([z.number(), z.string()])
            .describe('The amount of the token to swap from'),
        amount_out_minimum: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the token to swap to, defaults to 0')
            .optional()
            .default('0'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AerodromeSlipstreamBuyExactlyRequest = z
    .object({
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        tick_spacing: z.number().int().gte(1).describe('The tick spacing of the pool'),
        amount_out: z
            .union([z.number(), z.string()])
            .describe('The amount of the token to swap to'),
        amount_in_maximum: z
            .union([z.number(), z.string()])
            .describe('The maximum amount of the token to swap from'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AerodromeSlipstreamMintLiquidityProvisionRequest = z
    .object({
        token0: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token1: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        tick_spacing: z.number().int().gte(1).describe('The tick spacing of the pool'),
        tick_lower: z
            .number()
            .int()
            .describe('The lower tick of the range to mint the position in'),
        tick_upper: z
            .number()
            .int()
            .describe('The upper tick of the range to mint the position in'),
        amount0_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the first token to deposit'),
        amount1_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the second token to deposit'),
        amount0_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the first token to deposit'),
        amount1_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the second token to deposit'),
        recipient: z
            .union([z.string(), z.null()])
            .describe('The address that will receive the LP tokens')
            .optional(),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AerodromeSlipstreamIncreaseLiquidityProvisionRequest = z
    .object({
        token_id: z
            .number()
            .int()
            .describe('Token ID of the NFT representing the liquidity provisioned position.'),
        amount0_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the first token to deposit'),
        amount1_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the second token to deposit'),
        amount0_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the first token to deposit'),
        amount1_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the second token to deposit'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AerodromeSlipstreamWithdrawLiquidityProvisionRequest = z
    .object({
        token_id: z
            .number()
            .int()
            .describe('Token ID of the NFT representing the liquidity provisioned position.'),
        percentage_for_withdrawal: z
            .union([z.number(), z.string()])
            .describe('How much liquidity to take out in percentage.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AerodromeSlipstreamGetLiquidityProvisionPositionsRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z
            .string()
            .describe('The address of the user to check the balance of')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const AerodromePosition = z
    .object({
        nonce: z.number().int(),
        operator: z.string(),
        token0: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token1: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        tick_spacing: z.number().int(),
        tick_lower: z.number().int(),
        tick_upper: z.number().int(),
        liquidity: z.number().int(),
        fee_growth_inside0_last_x128: z.number().int(),
        fee_growth_inside1_last_x128: z.number().int(),
        tokens_owed0: z.number().int(),
        tokens_owed1: z.number().int(),
        token_id: z.number().int(),
    })
    .passthrough();
const AerodromeLPPositionsResponse = z
    .object({
        positions: z
            .record(AerodromePosition)
            .describe(`Liquidity provision positions belonging to a particular user. The key is a
tuple of the token0, token1, tick_spacing, tick_lower, and tick_upper of the position.`),
    })
    .passthrough();
const AerodromeSlipstreamGetPoolPriceRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        tick_spacing: z.number().int().gte(1).describe('The tick spacing of the pool'),
    })
    .passthrough();
const AerodromeSlipstreamPoolPriceResponse = z
    .object({
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        price: z
            .string()
            .describe(`The price of the pool. This is expressed as an instantaneous amount of how
many token0 you need to buy 1 token1. In any swap this will not change during the trade; use
the quote endpoint to get a better idea of how much you will pay!`),
        tick: z
            .number()
            .int()
            .describe(`The current tick in the pool. This is a number that represents the price of
the pool according to the aerodrome_slipstream v3 concentrated liquidity concept.`),
    })
    .passthrough();
const PortfolioRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z.string().describe('The address of the user.'),
    })
    .passthrough();
const TokenBalance = z
    .object({
        amount: z.string().describe('Amount of tokens a particular address holds'),
        decimals: z.number().int().describe('Number of decimals of the token'),
        token_symbol: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_address: z.string().describe('Address of the token'),
        price: z.string().describe('Price of the token in USD'),
        token_value_in_usd: z.string().describe('Value of the token balance in USD'),
    })
    .passthrough();
const Portfolio = z
    .object({
        total_value_in_usd: z.string().describe('Total value of the portfolio in USD'),
        token_balances: z.array(TokenBalance).describe('List of token balances in the portfolio'),
    })
    .passthrough();
const VisualizePortfolioRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z.string().describe('The address of the user.'),
    })
    .passthrough();
const Image = z.object({ image: z.string().describe('Base64 encoded SVG image') }).passthrough();
const PriceRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        token: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
    })
    .passthrough();
const PriceResponse = z
    .object({
        token_price_in_usd: z.string().describe('Price of the token in USD'),
    })
    .passthrough();
const TokensRequest = z.object({ chain: Chain.describe('The chain to use.') }).passthrough();
const TokenInfo = z
    .object({
        tokens: z.array(Token).describe('List of supported tokens for a given chain'),
    })
    .passthrough();
const GetErc20BalanceRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z.string().describe('The user to get the ERC20 balance of.'),
        token: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
    })
    .passthrough();
const BalanceInfoResponse = z
    .object({
        amount: z.string().describe('Amount of tokens a particular address holds'),
        decimals: z.number().int().describe('Number of decimals of the token'),
        token_symbol: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_address: z.string().describe('Address of the token'),
    })
    .passthrough();
const ContractName = z.enum([
    'AaveV3Pool',
    'AaveV3Oracle',
    'AaveV3ProtocolDataProvider',
    'AerodromeBasicFactory',
    'AerodromeSlipstreamFactory',
    'AerodromeBasicRouter',
    'AerodromeSlipstreamRouter',
    'AerodromeBasicPool',
    'AerodromeSlipstreamPool',
    'AerodromeSlipstreamNonfungiblePositionManager',
    'UniswapV3Pool',
    'UniswapV3Router',
    'UniswapV3Factory',
    'UniswapV3NFTPositionManager',
    'UniswapV3Quoter',
    'ChainlinkEACAggregatorProxy',
    'Multicall',
]);
const GetErc20AllowanceRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z.string().describe('The user to get the ERC20 allowance of.'),
        token: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        contract_name: ContractName.describe(`Select the protocol.

E.g. for increasing ERC-20 allowance.`),
    })
    .passthrough();
const AllowanceInfoResponse = z
    .object({
        amount: z.string().describe('Amount of tokens allowed to be spent by spender'),
        decimals: z.number().int().describe('Number of decimals of the token'),
        token_symbol: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_address: z.string().describe('Address of the token'),
        contract_address: z.string().describe('Address of the contract'),
    })
    .passthrough();
const GetEnsDetailsRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        ens_name: z.string().describe('The ENS address of the user.'),
    })
    .passthrough();
const EnsNameInfoResponse = z
    .object({
        wallet_address: z.string().describe('The wallet address of the user'),
        registrant: z.string().describe('The registrant of the ENS'),
    })
    .passthrough();
const WrapEthRequest = z
    .object({
        amount: z.union([z.number(), z.string()]).describe('The amount of ETH to wrap.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UnwrapWethRequest = z
    .object({
        amount: z.union([z.number(), z.string()]).describe('The amount of WETH to unwrap.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const TransferERC20Request = z
    .object({
        amount: z.union([z.number(), z.string()]).describe('Amount of token to transfer'),
        token: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        to: z.string().describe('The recipient of the tokens.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const TransferEthRequest = z
    .object({
        amount: z.union([z.number(), z.string()]).describe('Amount of ETH to transfer'),
        to: z.string().describe('The recipient of the ETH.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const IncreaseAllowanceRequest = z
    .object({
        token: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        contract_name: ContractName.describe(`Select the protocol.

E.g. for increasing ERC-20 allowance.`),
        amount: z
            .union([z.number(), z.string()])
            .describe('The amount of tokens to increase the allowance by.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const FeeEnum = z.enum(['0.01', '0.05', '0.3', '1.0']);
const UniswapBuyExactlyRequest = z
    .object({
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        fee: FeeEnum.describe(`The transaction fee of a Uniswap pool in bips.

Uniswap supports 4 different fee levels.`),
        amount_out: z
            .union([z.number(), z.string()])
            .describe('The amount of the token to swap to'),
        amount_in_maximum: z
            .union([z.number(), z.string()])
            .describe('The maximum amount of the token to swap from'),
        wrap_eth: z
            .boolean()
            .describe('Whether to wrap ETH to WETH, only use when swapping WETH into something')
            .optional()
            .default(false),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UniswapSellExactlyRequest = z
    .object({
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        fee: FeeEnum.describe(`The transaction fee of a Uniswap pool in bips.

Uniswap supports 4 different fee levels.`),
        amount_in: z
            .union([z.number(), z.string()])
            .describe('The amount of the token to swap from'),
        amount_out_minimum: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the token to swap to, defaults to 0')
            .optional()
            .default('0'),
        wrap_eth: z
            .boolean()
            .describe('Whether to wrap ETH to WETH, only use when swapping WETH into something')
            .optional()
            .default(false),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UniswapIncreaseLiquidityProvisionRequest = z
    .object({
        token_id: z
            .number()
            .int()
            .describe('Token ID of the NFT representing the liquidity provisioned position.'),
        amount0_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the first token to deposit'),
        amount1_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the second token to deposit'),
        amount0_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the first token to deposit'),
        amount1_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the second token to deposit'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UniswapMintLiquidityProvisionRequest = z
    .object({
        token0: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token1: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        fee: FeeEnum.describe(`The transaction fee of a Uniswap pool in bips.

Uniswap supports 4 different fee levels.`),
        tick_lower: z
            .number()
            .int()
            .gte(-887272)
            .lte(887272)
            .describe('The lower tick of the range to mint the position in'),
        tick_upper: z
            .number()
            .int()
            .gte(-887272)
            .lte(887272)
            .describe('The upper tick of the range to mint the position in'),
        amount0_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the first token to deposit'),
        amount1_desired: z
            .union([z.number(), z.string()])
            .describe('The desired amount of the second token to deposit'),
        amount0_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the first token to deposit'),
        amount1_min: z
            .union([z.number(), z.string()])
            .describe('The minimum amount of the second token to deposit'),
        recipient: z
            .union([z.string(), z.null()])
            .describe('The address that will receive the LP tokens')
            .optional(),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UniswapWithdrawLiquidityProvisionRequest = z
    .object({
        token_id: z
            .number()
            .int()
            .describe('Token ID of the NFT representing the liquidity provisioned position.'),
        percentage_for_withdrawal: z
            .union([z.number(), z.string()])
            .describe('How much liquidity to take out in percentage.'),
        chain: Chain.describe('The chain to use.'),
        sender: z
            .string()
            .describe('The address of the transaction sender')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UniswapGetBuyQuoteRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        fee: FeeEnum.describe(`The transaction fee of a Uniswap pool in bips.

Uniswap supports 4 different fee levels.`),
        amount_out: z
            .union([z.number(), z.string()])
            .describe('The amount of the token to swap to'),
    })
    .passthrough();
const UniswapBuyQuoteInfoResponse = z
    .object({
        amount_in: z
            .string()
            .describe('The amount of token_in you would need to give to the pool.'),
        price_after: z
            .string()
            .describe(
                'The price of the pool after this trade would happen. (How much token0 you need to buy 1 token1.)'
            ),
    })
    .passthrough();
const UniswapGetSellQuoteRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        fee: FeeEnum.describe(`The transaction fee of a Uniswap pool in bips.

Uniswap supports 4 different fee levels.`),
        amount_in: z
            .union([z.number(), z.string()])
            .describe('The amount of the token to swap from'),
    })
    .passthrough();
const UniswapSellQuoteInfoResponse = z
    .object({
        amount_out: z.string().describe('The amount of token_out you would receive from the pool.'),
        price_after: z
            .string()
            .describe(
                'The price of the pool after this trade would happen. (How much token0 you need to buy 1 token1.)'
            ),
    })
    .passthrough();
const UniswapGetPoolPriceRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        fee: FeeEnum.describe(`The transaction fee of a Uniswap pool in bips.

Uniswap supports 4 different fee levels.`),
    })
    .passthrough();
const UniswapPoolPriceResponse = z
    .object({
        token_in: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        token_out: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
        price: z
            .string()
            .describe(
                'The price of the pool. This is expressed as an instantanteous amount of how many token0 you need to buy 1 token1. In any swap this will not change during the trade; use the quote endpoint to get a better idea of how much you will pay!'
            ),
        tick: z
            .number()
            .int()
            .describe(
                'The current tick in the pool. This is a number that represents the price of the pool according to the uniswap v3 concentrated liquidity concept.'
            ),
    })
    .passthrough();
const UniswapCheckInRangeRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        token_id: z
            .number()
            .int()
            .gte(0)
            .describe('Token ID of the NFT representing the liquidity provisioned position.'),
    })
    .passthrough();
const UniswapCheckInRangeResponse = z
    .object({
        in_range: z
            .boolean()
            .describe(
                'Whether the position is in active tick range or not. If not in range, the position is not earning trading fees.'
            ),
    })
    .passthrough();
const UniswapGetLiquidityProvisionPositionsRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        user: z
            .string()
            .describe('The address of the user to check the balance of')
            .default('0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B'),
    })
    .passthrough();
const UniswapPositionsSolidityResponse = z
    .object({
        nonce: z.number().int(),
        operator: z.string(),
        token0: z.string(),
        token1: z.string(),
        fee: z.number().int(),
        tick_lower: z.number().int(),
        tick_upper: z.number().int(),
        liquidity: z.number().int(),
        fee_growth_inside0_last_x128: z.number().int(),
        fee_growth_inside1_last_x128: z.number().int(),
        tokens_owed0: z.number().int(),
        tokens_owed1: z.number().int(),
    })
    .passthrough();
const UniswapLPPositionsInfoResponse = z
    .object({
        positions: z
            .record(UniswapPositionsSolidityResponse)
            .describe(` Liquidity provision positions belonging to a particular user keyed by the
        token of owner index of the position. `),
    })
    .passthrough();
const AddressRequest = z
    .object({
        chain: Chain.describe('The chain to use.'),
        token: Token.describe(`A class representing the token.

This class is used to represent the token in the system. Notice individual
endpoints' documentation where per chain tokens are presented.`),
    })
    .passthrough();
const AddressResponse = z
    .object({ address: z.string().describe('Address of the token provided') })
    .passthrough();

export const schemas = {
    Token,
    Chain,
    AaveSupplyRequest,
    UnsignedTransaction,
    ValidationError,
    HTTPValidationError,
    InterestRateMode,
    AaveBorrowRequest,
    AaveRepayRequest,
    AaveWithdrawRequest,
    AaveGetAssetPriceRequest,
    AaveAssetPriceResponse,
    AaveGetLiquidityChangeRequest,
    AaveLiquidityChangeResponse,
    AaveGetUserPositionSummaryRequest,
    AaveUserPositionSummaryResponse,
    AaveGetUserPositionPerTokenRequest,
    AaveUserPositionPerTokenResponse,
    AerodromeSlipstreamSellExactlyRequest,
    AerodromeSlipstreamBuyExactlyRequest,
    AerodromeSlipstreamMintLiquidityProvisionRequest,
    AerodromeSlipstreamIncreaseLiquidityProvisionRequest,
    AerodromeSlipstreamWithdrawLiquidityProvisionRequest,
    AerodromeSlipstreamGetLiquidityProvisionPositionsRequest,
    AerodromePosition,
    AerodromeLPPositionsResponse,
    AerodromeSlipstreamGetPoolPriceRequest,
    AerodromeSlipstreamPoolPriceResponse,
    PortfolioRequest,
    TokenBalance,
    Portfolio,
    VisualizePortfolioRequest,
    Image,
    PriceRequest,
    PriceResponse,
    TokensRequest,
    TokenInfo,
    GetErc20BalanceRequest,
    BalanceInfoResponse,
    ContractName,
    GetErc20AllowanceRequest,
    AllowanceInfoResponse,
    GetEnsDetailsRequest,
    EnsNameInfoResponse,
    WrapEthRequest,
    UnwrapWethRequest,
    TransferERC20Request,
    TransferEthRequest,
    IncreaseAllowanceRequest,
    FeeEnum,
    UniswapBuyExactlyRequest,
    UniswapSellExactlyRequest,
    UniswapIncreaseLiquidityProvisionRequest,
    UniswapMintLiquidityProvisionRequest,
    UniswapWithdrawLiquidityProvisionRequest,
    UniswapGetBuyQuoteRequest,
    UniswapBuyQuoteInfoResponse,
    UniswapGetSellQuoteRequest,
    UniswapSellQuoteInfoResponse,
    UniswapGetPoolPriceRequest,
    UniswapPoolPriceResponse,
    UniswapCheckInRangeRequest,
    UniswapCheckInRangeResponse,
    UniswapGetLiquidityProvisionPositionsRequest,
    UniswapPositionsSolidityResponse,
    UniswapLPPositionsInfoResponse,
    AddressRequest,
    AddressResponse,
};

const endpoints = makeApi([
    {
        method: 'post',
        path: '/v0/aave/asset_price/get',
        description: `This endpoint retrieves the current price of a specified asset in USD as
determined by the Aave protocol.

It utilizes the Aave V3 Oracle to fetch the asset price, ensuring accurate and up-
to-date information. The request requires the asset identifier and the blockchain
network (chain) on which the asset resides. The response provides the asset price in
a standardized format, converted from Wei to the base currency decimals defined by
Aave.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveGetAssetPriceRequest.default({
                    chain: 'arbitrum:mainnet',
                    asset: 'USDC',
                }),
            },
        ],
        response: z
            .object({ price: z.string().describe('The price of the asset in USD.') })
            .passthrough(),
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aave/borrow',
        description: `You will pay interest for your borrows.

Price changes in the assets may lead to some or all of your collateral being
liquidated, if the borrow position becomes unhealthy.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveBorrowRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    asset: 'USDT',
                    amount: 1,
                    interest_rate_mode: 'variable',
                    on_behalf_of: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aave/liquidity/change/get',
        description: `This endpoint retrieves the change in the reserve liquidity index between two
provided blocks.

This is then converted to a percentage change. The liquidity index represents the
change in debt and interest accrual over each block. Aave does not store individual
user balances directly. Instead, it keeps a scaled balance and uses the liquidity
index to compute real balances dynamically. If a user was to have deposited tokens
at the start block, a positive liquidity index change will represent accrued
interest and a profit. If tokens were borrowed at the start block, this debt will
increase, compound on itself and represent large debt. The reverse in both cases is
true if the liquidity index is negative.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveGetLiquidityChangeRequest.default({
                    chain: 'arbitrum:mainnet',
                    start_block: 0,
                    end_block: 319407231,
                    asset: 'USDC',
                }),
            },
        ],
        response: AaveLiquidityChangeResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aave/repay',
        description: `This endpoint allows users to repay a portion or the entirety of their borrowed
tokens on the Aave platform.

By repaying borrowed amounts, users can improve their health factor, which is a
measure of the safety of their loan position. A higher health factor reduces the
risk of liquidation, ensuring a more secure borrowing experience. The endpoint
requires specifying the chain and the details of the repayment transaction,
including the amount and the asset to be repaid.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveRepayRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    asset: 'USDT',
                    amount: 1,
                    interest_rate_mode: 'variable',
                    on_behalf_of: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aave/supply',
        description: `By supplying assets, users can earn interest on their deposits.

The supplied collateral can be used as a basis for borrowing other assets, allowing
users to leverage their positions. In combination with a trading protocol, this can
create leverage.

Overall, this endpoint is a critical component for users looking to maximize their
asset utility within the AAVEv3 ecosystem, providing both earning potential and
borrowing flexibility.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveSupplyRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    asset: 'USDC',
                    amount: 1,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aave/user_position_per_token/get',
        description: `This endpoint retrieves the user&#x27;s position for a specific token on the AAVE
platform.

It provides key financial metrics including the current aToken balance, current
stable debt, current variable debt, principal stable debt, principal variable debt,
stable borrow rate, stable borrow rate for new loans, variable borrow rate, and
liquidity rate. These metrics are calculated by aggregating data across all open
positions held by the user for the specified token, offering a detailed view of
their financial standing within the AAVE ecosystem.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveGetUserPositionPerTokenRequest.default({
                    chain: 'arbitrum:mainnet',
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    asset: 'USDC',
                }),
            },
        ],
        response: AaveUserPositionPerTokenResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aave/user_position_summary/get',
        description: `This endpoint retrieves a comprehensive summary of a user&#x27;s position on the AAVE
platform.

It provides key financial metrics including the total collateral deposited, total
debt accrued, available borrowing capacity, liquidation threshold, maximum loan-to-
value ratio, and the health factor of the user&#x27;s account. These metrics are
calculated by aggregating data across all open positions held by the user, offering
a holistic view of their financial standing within the AAVE ecosystem.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveGetUserPositionSummaryRequest.default({
                    chain: 'arbitrum:mainnet',
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: AaveUserPositionSummaryResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aave/withdraw',
        description: `This endpoint facilitates the withdrawal of collateral from the Aave protocol.

Users can withdraw a portion or all of their collateral, which may increase the risk
of liquidation if there are outstanding borrows. The withdrawal process also
includes the collection of any interest earned on the collateral. It is important
for users to carefully consider their outstanding debts and the potential impact on
their liquidation threshold before proceeding with a withdrawal. This endpoint is
designed to provide a seamless and efficient way to manage your collateral within
the Aave ecosystem.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AaveWithdrawRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    asset: 'USDC',
                    amount: 1,
                    recipient: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aerodrome_slipstream/liquidity_provision/increase',
        description: `Increase the liquidity of an existing Liquidity Provider (LP) position.

This endpoint allows users to add more tokens to their current LP position,
enhancing their participation in liquidity provision. By increasing liquidity, users
can potentially earn more rewards and improve their position in the pool. The
process involves specifying additional token amounts and updating the pool details.
The response will confirm the successful increase of the LP position, providing
users with updated information about their enhanced position. This functionality is
vital for users aiming to optimize their liquidity provision strategy, enabling them
to adapt to market conditions and maximize their returns in decentralized finance
(DeFi) markets.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AerodromeSlipstreamIncreaseLiquidityProvisionRequest.default({
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    chain: 'base:mainnet',
                    token_id: 10433247,
                    amount0_desired: 0.1,
                    amount1_desired: 0.1,
                    amount0_min: 0,
                    amount1_min: 0,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aerodrome_slipstream/liquidity_provision/mint',
        description: `Initiate a new Liquidity Provider (LP) position by minting tokens.

This endpoint allows users to open a new LP position, enabling them to participate
in liquidity provision. The minting process involves creating a new position with
specified parameters, such as token amounts and pool details. The response will
confirm the successful creation of the LP position, providing users with the
necessary information to manage their newly minted position. This functionality is
crucial for users looking to expand their liquidity provision activities, offering
them the opportunity to engage in decentralized finance (DeFi) markets effectively.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AerodromeSlipstreamMintLiquidityProvisionRequest.default({
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    chain: 'base:mainnet',
                    token0: 'WETH',
                    token1: 'USDT',
                    tick_spacing: 100,
                    tick_lower: -300000,
                    tick_upper: 300000,
                    amount0_desired: 0.1,
                    amount1_desired: 0.000048,
                    amount0_min: 0,
                    amount1_min: 0,
                    recipient: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aerodrome_slipstream/liquidity_provision/positions/get',
        description: `Retrieve the total number of Liquidity Provider (LP) positions associated with a
specific sender.

This endpoint allows users to query and obtain detailed information about their LP
positions, including the number of active positions they hold. The response model,
AerodromeLPPositionsInfo, provides a structured representation of the LP positions
data, ensuring clarity and ease of use. This functionality is essential for users
managing their liquidity provision activities, enabling them to make informed
decisions based on their current positions.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AerodromeSlipstreamGetLiquidityProvisionPositionsRequest.default({
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    chain: 'base:mainnet',
                }),
            },
        ],
        response: AerodromeLPPositionsResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aerodrome_slipstream/liquidity_provision/withdraw',
        description: `Withdraw an existing Liquidity Provider (LP) position.

This endpoint allows users to remove their tokens from an LP position, effectively
closing their participation in the liquidity pool. The withdrawal process involves
specifying the LP position to be closed, and the response will confirm the
successful removal of liquidity, providing users with details about the withdrawn
tokens and any remaining balances. This functionality is essential for users who
wish to exit their liquidity provision activities, enabling them to reclaim their
assets and potentially reallocate them to other investment opportunities. The
endpoint ensures a smooth and secure withdrawal process, facilitating users&#x27;
strategic management of their decentralized finance (DeFi) portfolios.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AerodromeSlipstreamWithdrawLiquidityProvisionRequest.default({
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    chain: 'base:mainnet',
                    token_id: 10433247,
                    percentage_for_withdrawal: 1,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aerodrome_slipstream/pool_price/get',
        description: `This endpoint retrieves the current price of a pool, indicating how many token0
you can purchase for 1 token1.

Note that this is an instantaneous price and may change during any trade. For a more
accurate representation of the trade ratios between the two assets, consider using
the quote endpoint.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AerodromeSlipstreamGetPoolPriceRequest.default({
                    chain: 'base:mainnet',
                    token_in: 'USDC',
                    token_out: 'WETH',
                    tick_spacing: 100,
                }),
            },
        ],
        response: AerodromeSlipstreamPoolPriceResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aerodrome_slipstream/swap/buy_exactly',
        description: `This endpoint facilitates the trading of tokens by allowing users to specify the
exact amount of the output token they wish to receive.

Utilizing the Aerodrome Slipstream protocol, the system calculates the necessary
amount of the input token required to achieve the desired output. This operation is
particularly useful for users who have a specific target amount of the output token
in mind and are willing to provide the corresponding input token amount. The
transaction is executed with consideration of current market conditions, including
liquidity and price impact, ensuring that the trade is completed efficiently and
effectively.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AerodromeSlipstreamBuyExactlyRequest.default({
                    chain: 'base:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token_in: 'USDC',
                    token_out: 'WETH',
                    tick_spacing: 100,
                    amount_out: 0.000048,
                    amount_in_maximum: 0.1,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/aerodrome_slipstream/swap/sell_exactly',
        description: `This endpoint allows users to trade a specific amount of one token into another
token using the Aerodrome Slipstream protocol.

The transaction is executed by specifying the exact amount of the input token to be
sold, and the system calculates the amount of the output token that will be
received. The operation ensures that the trade is conducted within the constraints
of the current market conditions, taking into account the liquidity and price
impact. This endpoint is suitable for users who want to sell a precise quantity of a
token and are willing to accept the resulting amount of the other token.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AerodromeSlipstreamSellExactlyRequest.default({
                    chain: 'base:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token_in: 'USDC',
                    token_out: 'WETH',
                    tick_spacing: 100,
                    amount_in: 1,
                    amount_out_minimum: 0,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/allowance/get',
        description: `In decentralized finance (DeFi) protocols such as Uniswap or AAVE, users must set
a token allowance to authorize the protocol to spend a specified amount of their
tokens on their behalf.

This is a crucial step before engaging in any transactions or operations within
these protocols, ensuring that the protocol has the necessary permissions to manage
the user&#x27;s tokens securely and efficiently.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: GetErc20AllowanceRequest.default({
                    chain: 'arbitrum:mainnet',
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token: 'USDC',
                    contract_name: 'AaveV3Pool',
                }),
            },
        ],
        response: AllowanceInfoResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/allowance/set',
        description: `This endpoint allows users to modify the token allowance for a specific protocol.

In decentralized finance (DeFi), setting an allowance is a necessary step to
authorize a protocol to spend a specified amount of tokens on behalf of the user.
This operation is crucial for ensuring that the protocol can manage the user&#x27;s
tokens securely and efficiently, enabling seamless transactions and operations
within the DeFi ecosystem.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: IncreaseAllowanceRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token: 'USDC',
                    contract_name: 'AaveV3Pool',
                    amount: 1,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/balance/get',
        description: `Returns the balance of a specific ERC20 token for a given user address.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: GetErc20BalanceRequest.default({
                    chain: 'arbitrum:mainnet',
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token: 'USDC',
                }),
            },
        ],
        response: BalanceInfoResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/ens/get',
        description: `An ENS name is a string ending in &#x60;.eth&#x60;.

E.g. &#x60;vitalik.eth&#x60;. This endpoint can be used to
query the actual ethereum wallet address behind the ENS name.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: GetEnsDetailsRequest.default({
                    chain: 'ethereum:mainnet',
                    ens_name: 'vitalik.eth',
                }),
            },
        ],
        response: EnsNameInfoResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/portfolio/get',
        description: `Fetch the detailed portfolio of a specific wallet address on a given blockchain.

This includes the total value of the portfolio in USD and a breakdown of token
balances, including their respective values and quantities.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: PortfolioRequest.default({
                    chain: 'arbitrum:mainnet',
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: Portfolio,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/price/usd/get',
        description: `Retrieves the price of the specified token relative to USD using Chainlink&#x27;s on-
chain price feeds.

Chainlink is a decentralized oracle that aggregates price data from off-chain
sources. This ensures the price is tamper-resistant but the price might be stale
with the update frequency of the oracle.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: PriceRequest.default({
                    chain: 'arbitrum:mainnet',
                    token: 'WBTC',
                }),
            },
        ],
        response: z
            .object({
                token_price_in_usd: z.string().describe('Price of the token in USD'),
            })
            .passthrough(),
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/supported_tokens/get',
        description: `Get the list of supported tokens on a chain by the Compass API.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: TokensRequest.default({ chain: 'arbitrum:mainnet' }),
            },
        ],
        response: TokenInfo,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/transfer/erc20',
        description: `Sends ERC20 tokens from the sender&#x27;s address to the specified recipient.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: TransferERC20Request.default({
                    chain: 'arbitrum:mainnet',
                    to: '0xEe0748088fe5D752B877656d717B279DaE630Ce2',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token: 'USDC',
                    amount: 0.1,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/transfer/native_token',
        description: `Sends native ETH from the sender&#x27;s address to the specified recipient.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: TransferEthRequest.default({
                    chain: 'arbitrum:mainnet',
                    to: '0x7Fd9DBad4d8B8F97BEdAC3662A0129a5774AdA8E',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    amount: 0.000048,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/unwrap_weth',
        description: `Unwrapping WETH converts the ERC-20 compliant form of ETH back to native ETH that
can be used for gas and other native purposes.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UnwrapWethRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    amount: 0.0000048,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/visualize_portfolio/get',
        description: `Generate a visual representation of the token portfolio for a wallet address.

The response is an SVG image of a pie chart depicting the relative distribution of
tokens held, colored and labeled with token symbols, percentages and token values in
USD.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: VisualizePortfolioRequest.default({
                    chain: 'arbitrum:mainnet',
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: z
            .object({ image: z.string().describe('Base64 encoded SVG image') })
            .passthrough(),
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/generic/wrap_eth',
        description: `Wrapping ETH creates an ERC-20 compliant form of ETH that is typically needed for
it to be traded on DeFi protocols.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: WrapEthRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    amount: 0.0000048,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/token/address/get',
        description: `Get the address for a token.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: AddressRequest.default({
                    chain: 'arbitrum:mainnet',
                    token: 'WETH',
                }),
            },
        ],
        response: z
            .object({ address: z.string().describe('Address of the token provided') })
            .passthrough()
            .default({ address: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B' }),
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/liquidity_provision/in_range/get',
        description: `This endpoint allows users to check whether a specific liquidity provider ()
position is within the active tick range on the uniswap platform.

by providing the token id associated with the position, users can verify if the
position is currently within the tick range where trading occurs. this information
is essential for users to monitor the status of their lp positions and ensure that
they are actively participating in the trading activities within the liquidity pool
and earning trading fees.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapCheckInRangeRequest.default({
                    chain: 'arbitrum:mainnet',
                    token_id: 4318185,
                }),
            },
        ],
        response: z
            .object({
                in_range: z
                    .boolean()
                    .describe(
                        'Whether the position is in active tick range or not. If not in range, the position is not earning trading fees.'
                    ),
            })
            .passthrough(),
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/liquidity_provision/increase',
        description: `This endpoint allows users to increase their existing Liquidity Provider (LP)
positions on the Uniswap platform.

By providing the necessary parameters, users can add more liquidity to their current
positions, thereby increasing their stake in the liquidity pool. This operation is
beneficial for users who wish to enhance their potential earnings from trading fees
within the pool. The endpoint requires details such as the token pair, additional
amount to be added, and any other parameters necessary for the liquidity increase
process.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapIncreaseLiquidityProvisionRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token_id: 4318185,
                    amount0_desired: 0.1,
                    amount1_desired: 0.1,
                    amount0_min: 0.05,
                    amount1_min: 0.05,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/liquidity_provision/mint',
        description: `This endpoint allows users to open a new Liquidity Provider (LP) position on the
Uniswap platform.

By providing the necessary parameters, users can initiate a minting process to
create a new LP token, which represents their stake in a specific liquidity pool.
This operation is essential for users looking to participate in liquidity provision,
enabling them to earn fees from trades that occur within the pool. The endpoint
requires details such as the token pair, amount, and any additional parameters
needed for the minting process.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapMintLiquidityProvisionRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token0: 'USDC',
                    token1: 'DAI',
                    fee: '0.01',
                    tick_lower: -1000,
                    tick_upper: 1000,
                    amount0_desired: 0.1,
                    amount1_desired: 0.1,
                    amount0_min: 0,
                    amount1_min: 0,
                    recipient: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/liquidity_provision/positions/get',
        description: `This endpoint retrieves the number of Liquidity Provider (LP) positions
associated with a specific sender address on the Uniswap platform.

Users can query this endpoint to obtain detailed information about their LP
positions, including the total number of positions and relevant metadata. This
information is crucial for users to manage and analyze their liquidity provision
activities effectively.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapGetLiquidityProvisionPositionsRequest.default({
                    chain: 'arbitrum:mainnet',
                    user: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                }),
            },
        ],
        response: UniswapLPPositionsInfoResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/liquidity_provision/withdraw',
        description: `This endpoint allows users to withdraw their Liquidity Provider (LP) positions
from the Uniswap platform.

By specifying the necessary parameters, users can initiate the withdrawal process to
remove their stake from a specific liquidity pool. This operation is crucial for
users who wish to reclaim their assets or reallocate their liquidity to different
pools or investments. The endpoint requires details such as the token pair, the
amount to be withdrawn, and any additional parameters needed for the withdrawal
process. Users should ensure they meet any protocol requirements or conditions
before initiating a withdrawal to avoid potential issues or penalties.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapWithdrawLiquidityProvisionRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token_id: 4318185,
                    percentage_for_withdrawal: 1,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/pool_price/get',
        description: `This endpoint calculates the price of a token in a Uniswap pool.

The price is calculated based on the current pool state and the specified fee tier.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapGetPoolPriceRequest.default({
                    chain: 'arbitrum:mainnet',
                    token_in: 'USDC',
                    token_out: 'USDT',
                    fee: '0.01',
                }),
            },
        ],
        response: UniswapPoolPriceResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/quote/buy_exactly/get',
        description: `This endpoint calculates the amount of input tokens required to purchase a
specified amount of output tokens from a Uniswap pool.

It also provides the resulting price after the transaction. The calculation takes
into account the current pool state and the specified fee tier.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapGetBuyQuoteRequest.default({
                    chain: 'arbitrum:mainnet',
                    token_in: 'USDC',
                    token_out: 'USDT',
                    fee: '0.01',
                    amount_out: 1,
                }),
            },
        ],
        response: UniswapBuyQuoteInfoResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/quote/sell_exactly/get',
        description: `This endpoint calculates the amount of input tokens required to purchase a
specified amount of output tokens from a Uniswap pool.

It also provides the resulting price after the transaction. The calculation takes
into account the current pool state and the specified fee tier.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapGetSellQuoteRequest.default({
                    chain: 'arbitrum:mainnet',
                    token_in: 'USDC',
                    token_out: 'USDT',
                    fee: '0.01',
                    amount_in: 1,
                }),
            },
        ],
        response: UniswapSellQuoteInfoResponse,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/swap/buy_exactly',
        description: `This endpoint allows users to trade a variable amount of one token to receive an
exact amount of another token using the Uniswap protocol.

The transaction is executed on the specified blockchain network, and the user must
provide the necessary transaction details, including the token to buy, the token to
pay with, and the exact amount to receive. If the token being paid with is WETH and
needs to be wrapped, the appropriate amount will be wrapped automatically.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapBuyExactlyRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token_in: 'USDC',
                    token_out: 'USDT',
                    fee: '0.01',
                    amount_out: 1,
                    amount_in_maximum: 1.1,
                    wrap_eth: false,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
    {
        method: 'post',
        path: '/v0/uniswap/swap/sell_exactly',
        description: `This endpoint allows users to trade a specific amount of one token into another
token using the Uniswap protocol.

The transaction is executed on the specified blockchain network, and the user must
provide the necessary transaction details, including the token to sell, the token to
receive, and the amount to sell. If the token being sold is WETH and needs to be
wrapped, the appropriate amount will be wrapped automatically.`,
        requestFormat: 'json',
        parameters: [
            {
                name: 'body',
                type: 'Body',
                schema: UniswapSellExactlyRequest.default({
                    chain: 'arbitrum:mainnet',
                    sender: '0x29F20a192328eF1aD35e1564aBFf4Be9C5ce5f7B',
                    token_in: 'USDC',
                    token_out: 'USDT',
                    fee: '0.01',
                    amount_in: 1,
                    amount_out_minimum: 0.5,
                    wrap_eth: false,
                }),
            },
        ],
        response: UnsignedTransaction,
        errors: [
            {
                status: 422,
                description: `Validation Error`,
                schema: HTTPValidationError,
            },
        ],
    },
]);

export const api = new Zodios(endpoints);

export function createApiClient(baseUrl: string, options?: ZodiosOptions) {
    const defaultHeaders = {
        'x-compass-origin': 'ts-sdk',
    };

    const finalOptions: ZodiosOptions = {
        ...options,
        axiosConfig: {
            ...options?.axiosConfig,
            headers: {
                ...defaultHeaders,
                ...options?.axiosConfig?.headers,
            },
        },
    };

    return new Zodios(baseUrl, endpoints, finalOptions);
}
