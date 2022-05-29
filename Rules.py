import json


class Rules():
    def __init__(self):
        with open("pricing_policy.json") as f:
            self.pricing = json.load(f)

    def getPrice(self, item, amount):
        price = 0
        if item.name in self.pricing:
            sorted_prices = dict(sorted(self.pricing[item.name].items(), key=lambda item: item[1], reverse=True))
            for n in sorted_prices:
                price += (amount // int(n)) * sorted_prices[n]
                amount = amount % int(n)
        return price
