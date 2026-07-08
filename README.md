# **AI-Driven Trading Bot**

An automated algorithmic trading bot built in Python that leverages natural language processing to make data-driven market decisions. Built on the Lumibot framework and integrated with the Alpaca Trade API, this bot uses the FinBERT NLP model to analyze the sentiment of real-time financial news. It features robust risk management protocols and has been rigorously backtested to ensure strategy viability.

## Table of Contents

* [Features](https://github.com/wechring/AI-Driven-Trading-Bot#features)
* [Tech Stack](https://github.com/wechring/AI-Driven-Trading-Bot#tech-stack)
* [Prerequisites](https://github.com/wechring/AI-Driven-Trading-Bot#prerequisites)
* [Installation](https://github.com/wechring/AI-Driven-Trading-Bot#installation)
* [Configuration](https://github.com/wechring/AI-Driven-Trading-Bot#configuration)
* [Usage](https://github.com/wechring/AI-Driven-Trading-Bot#usage)
* [Disclaimer](https://github.com/wechring/AI-Driven-Trading-Bot#disclaimer)

## Features

* **Sentiment Analysis:** Integrates the FinBERT NLP model to evaluate financial news sentiment (bullish, bearish, or neutral) and generate automated trading signals.
* **Automated Execution:** Utilizes the Lumibot framework for streamlined, hands-off algorithmic trade execution.
* **Advanced Risk Management:** Implements dynamic position sizing, strict take-profit targets, and stop-loss enforcement to protect capital and mitigate downside risk.
* **Historical Backtesting:** The core trading strategy has been backtested against 4 years of historical market data to validate its efficacy and fine-tune risk parameters.
* **Live Market Data:** Seamlessly connects to the Alpaca Trade API to fetch live financial news, retrieve historical data, and execute trades.

## Tech Stack

* **Language:** Python 3.x
* **Framework:** Lumibot
* **Machine Learning/NLP:** FinBERT (Hugging Face)
* **Broker/Data API:** Alpaca Trade API


## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3.8 or higher installed.
* An active [Alpaca](https://www.google.com/search?q=https://alpaca.markets/) account with API keys generated (Paper Trading recommended for testing).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/wechring/AI-Driven-Trading-Bot
cd AI-Driven-Trading-Bot

```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

3. Install the required dependencies:

```bash
pip install -r requirements.txt

```

## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your Alpaca API credentials to the `.env` file:

```env
ALPACA_API_KEY=your_api_key_here
ALPACA_API_SECRET=your_api_secret_here
ALPACA_ENDPOINT=https://paper-api.alpaca.markets

```

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
