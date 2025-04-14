# langchain-compass

The Compass-LangChain toolkit contains tools which enable an LLM agent to perform onchain operations on major DeFi protocols.


# Setup

## Installation

```bash
pip install -U langchain-compass
```

## Environment Setup

```
# .env
OPENAI_API_KEY=your_openai_api_key_here
```

# Usage:

## List Tools in Toolkit:

```python
```

And you should configure credentials by setting the following environment variables:

Import this toolkit by
```python
from langchain_compass.toolkits import LangchainCompassToolkit
```

Compass requires an API key for some features. You can set the key as an environment variable
```bash
OPENAI_API_KEY="<Your-Compass-API-KEY>"
```