# **AI-Driven Trading Bot**

An automated algorithmic trading bot built in Python that leverages natural language processing to make data-driven market decisions. Built on the Lumibot framework and integrated with the Alpaca Trade API, this bot uses the FinBERT NLP model to analyze the sentiment of real-time financial news. It features robust risk management protocols and has been rigorously backtested to ensure strategy viability.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Disclaimer](#disclaimer)

## Features

* **Sentiment Analysis:** Integrates the FinBERT NLP model to evaluate financial news sentiment (bullish, bearish, or neutral) and generate automated trading signals.
* **Automated Execution:** Utilizes the Lumibot framework for streamlined, hands-off algorithmic trade execution.
* **Advanced Risk Management:** Implements dynamic position sizing, strict take-profit targets, and stop-loss enforcement to protect capital and mitigate downside risk.
* **Historical Backtesting:** The core trading strategy has been backtested against 4 years of historical market data to validate its efficacy and fine-tune risk parameters.
* **Live Market Data:** Seamlessly connects to the Alpaca Trade API to fetch live financial news, retrieve historical data, and execute trades.

## Tech Stack

* **Language:** Python 3.10
* **Framework:** Lumibot
* **Machine Learning/NLP:** FinBERT (Hugging Face Transformers / PyTorch)
* **Broker/Data API:** Alpaca Trade API


## Prerequisites

Before you begin, ensure you have met the following requirements:

* **Python 3.10** installed.
* An active [Alpaca](https://alpaca.markets/) account with API keys generated (Paper Trading recommended for testing).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/wechring/AI-Driven-Trading-Bot
cd AI-Driven-Trading-Bot

```

2. Create and activate a virtual environment (required):

```bash
python3.10 -m venv .venv
```
# On Mac use
```bash
source .venv/bin/activate  
```
# On Windows use 
```bash
.venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt

```

## Configuration

1. Duplicate the example environment file:


# On macOS/Linux:
```bash
cp .env.example .env
```
# On Windows:
```bash
copy .env.example .env
```

2. Open the newly created `.env` file and replace `your_api_key_here` and `your_api_secret_here` with your actual Alpaca (real or paper) trading credentials.


## Usage

To run a backtest using the historical data:

```bash
python backtest.py

```

To start the bot in live/paper trading mode:

```bash
python main.py

```

## Disclaimer

**This software is for educational purposes only.** Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. The authors and all affiliates assume no responsibility for your trading results.
