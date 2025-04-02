# @compass-labs/sdk

This package is a TypeScript SDK for [Compass API](https://api.compasslabs.ai/) created specifically for the use in AI Agents.

## Overview

The `@compass-labs/sdk` package is a TypeScript SDK designed to facilitate interaction with various blockchain protocols through a structured API. It is particularly useful for AI agents, such as [ElizaOS](https://github.com/elizaOS/eliza), that require seamless integration with blockchain functionalities.

## Features

- **Comprehensive API Client**: The package provides a robust API client built using `Zodios`, which allows for type-safe API requests and responses. This ensures that interactions with the API are reliable and less prone to runtime errors.

- **Blockchain Interactions**: The SDK includes a variety of endpoints for interacting with blockchain protocols, such as Uniswap, AAVE, Aerodrome, etc. These endpoints support operations like swapping tokens, removing liquidity, and fetching pool prices. The list of supported protocols and chains is expanded on a weekly basis. Feel free to contact [Compass Team](https://www.compasslabs.ai/) to include a protocol that you wish to use.

- **Type Safety**: Leveraging TypeScript and `zod` for schema validation, the package ensures that all data structures conform to expected formats. This reduces the likelihood of errors and enhances code maintainability.

## Usage

To use the `@compass-labs/sdk` package, you need to import the necessary modules and create an API client.

```
npm install @compass-labs/sdk
```

The API exposes two different endpoint types:

- **Read endpoints, ie endpoints making contract calls to retrieve on-chain data**

Example, getting asset prices according to AAVE Oracle.

```
import { createApiClient } from '@compass-labs/sdk';

const apiClient = createApiClient('https://api.compasslabs.ai');

apiClient["post"]("/v0/aave/asset_price/get", {"chain": "arbitrum:mainnet", "asset": "WETH"}).then((response: any) => {
    console.log(response);
}).catch((error: any) => {
    console.error(error);
});
```

Each read endpoint has its own response schema, this can be found in the [Compass API Docs](https://api.compasslabs.ai)

- **Unsigned transaction endpoints, ie endpoints generating an unsigned transcation to be broadcast to the blockchain**:

Example, supplying WETH on AAVE:

```
apiClient["post"]("/v0/aave/supply", {
    "chain": "arbitrum:mainnet",
    "sender": "0x8A2c9eD8F6B9aD09036Cc0F5AAcaE7E6708f3D0c",
    "asset": "WETH",
    "amount": 1.5,
    "on_behalf_of": "0x8A2c9eD8F6B9aD09036Cc0F5AAcaE7E6708f3D0c"
  }).then((response: any) => {
    console.log(response);
}).catch((error: any) => {
    console.error(error);
});
```

if the request is successful, an unsigned transaction of the following form will be returned:

```
{
    chainId: "The chain id of the transaction",
    data: "The data of the transaction",
    from: "The sender of the transaction",
    gas: "The gas of the transaction",
    to: "The recipient of the transaction",
    value: "The value of the transaction",
    nonce: "The nonce of the address",
    maxFeePerGas: "The max fee per gas of the transaction",
    maxPriorityFeePerGas: "The max priority fee per gas of the transaction",
}
```

this can be further signed and sent, example using `viem`'s `WalletClient`:

```
import { createWalletClient } from 'viem';

apiClient["post"]("/v0/aave/supply", {
    "chain": "arbitrum:mainnet",
    "sender": "0x8A2c9eD8F6B9aD09036Cc0F5AAcaE7E6708f3D0c",
    "asset": "WETH",
    "amount": 1.5,
    "on_behalf_of": "0x8A2c9eD8F6B9aD09036Cc0F5AAcaE7E6708f3D0c"
  }).then((response: any) => {
    const walletClient = createWalletClient(...);
    const txHash = await walletClient.sendTransaction(response);
    const txReceipt await walletClient.waitForTransactionReceipt({hash: txHash});
}).catch((error: any) => {
    console.error(error);
});
```
