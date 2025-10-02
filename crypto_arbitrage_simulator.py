#!/usr/bin/env python3
import random
from typing import List, Dict

class Exchange:
    def __init__(self, name: str, fee: float = 0.001):
        self.name = name
        self.fee = fee
        self.prices: Dict[str, float] = {}

    def update_price(self, symbol: str, price: float):
        self.prices[symbol] = price

    def get_effective_price(self, symbol: str, side: str):
        price = self.prices[symbol]
        return price * (1 + self.fee) if side == "buy" else price * (1 - self.fee)

class ArbitrageSimulator:
    def __init__(self, exchanges: List[Exchange], symbol: str):
        self.exchanges = exchanges
        self.symbol = symbol

    def simulate_day(self):
        # Update random prices for each exchange
        for ex in self.exchanges:
            base_price = 100 + random.uniform(-5,5)
            ex.update_price(self.symbol, base_price)

        # Find arbitrage opportunities
        opportunities = []
        for buy_ex in self.exchanges:
            for sell_ex in self.exchanges:
                if buy_ex == sell_ex:
                    continue
                buy_price = buy_ex.get_effective_price(self.symbol, "buy")
                sell_price = sell_ex.get_effective_price(self.symbol, "sell")
                profit = sell_price - buy_price
                if profit > 0:
                    opportunities.append({
                        "buy_from": buy_ex.name,
                        "sell_to": sell_ex.name,
                        "buy_price": round(buy_price,2),
                        "sell_price": round(sell_price,2),
                        "profit": round(profit,2)
                    })
        return opportunities

def demo():
    exchanges = [
        Exchange("Binance"),
        Exchange("Coinbase"),
        Exchange("Kraken")
    ]
    simulator = ArbitrageSimulator(exchanges, symbol="BTC")
    for day in range(1,6):
        opportunities = simulator.simulate_day()
        print(f"Day {day} Arbitrage Opportunities ({len(opportunities)} found):")
        for op in opportunities:
            print(op)
        print("-"*50)

if __name__ == "__main__":
    demo()
