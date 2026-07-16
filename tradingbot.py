import math
from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime, timedelta
from alpaca_trade_api.rest import REST, URL
from finbert_utils import predict_sentiment

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}


class MLTrader(Strategy):
    def initialize(self, index: str = "SPY", cash_risk: float = 0.1):
        self.index = index
        self.cash_risk = cash_risk
        self.sleeptime = "1D"
        self.api = REST(key_id=API_KEY, secret_key=API_SECRET,
                        base_url=BASE_URL)

    def position_sizing(self):
        cash = self.get_cash()
        last_price = self.get_last_price(self.index)
        if cash is not None and last_price is not None and last_price > 0:
            quantity = math.floor(cash * self.cash_risk / last_price)
            return cash, last_price, quantity

        return cash if cash is not None else 0, 0, 0

    def get_dates(self):
        today = self.get_datetime()
        start_date = today - timedelta(days=3)
        return today.strftime("%Y-%m-%d"), start_date.strftime("%Y-%m-%d")

    def get_sentiment(self):
        today, start_date = self.get_dates()
        try:
            news = self.api.get_news(self.index, start=start_date, end=today)
        except Exception as e:
            self.log_message(f"News fetch failed: {e}")
            return 0.0, "neutral"
        news = [event.headline for event in news]
        if not news:
            return 0.0, "neutral"
        probability, sentiment = predict_sentiment(news)
        return probability, sentiment

    def on_trading_iteration(self):
        probability, sentiment = self.get_sentiment()

        position = self.get_position(self.index)
        currently_long = position is not None and position.quantity > 0

        if sentiment == "positive" and probability > 0.99:
            if not currently_long:
                cash, last_price, quantity = self.position_sizing()
                if quantity > 0 and cash > last_price:
                    order = self.create_order(
                        self.index,
                        quantity=quantity,
                        side="buy",
                        type="bracket",
                        take_profit_price=last_price * 1.2,  # 20% profit target
                        stop_loss_price=last_price * 0.95,  # 5% stop loss
                    )
                    self.submit_order(order)

        elif sentiment == "negative" and probability > 0.99:
            if currently_long:
                self.sell_all()
            # order = self.create_order(
            #     self.index,
            #     quantity=quantity,
            #     side="sell",
            #     type="bracket",
            #     take_profit_price=last_price * 0.8,  # 20% profit target
            #     stop_loss_price=last_price * 1.05,  # 5% stop loss
            # )
            # self.submit_order(order)


start_date = datetime(2025, 6, 1)
end_date = datetime(2025, 12, 31)
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name="MLTrader", broker=broker,
                    parameters={
                        "index": "SPY",
                        "cash_risk": 0.5
                    })

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"index": "SPY", "cash_risk": 0.5},
)

# trader = Trader()
# trader.add_strategy(strategy)
# trader.run_all()
