import json


class Rules():

  def __init__(self):
    with open("pricing_policy.json") as f:
      self.pricing = json.load(f)

  def getPrice(self, item, amount):
    """
    Get the price of an item, given the
    name of the item and the amount of the
    item.

    This references the pricing policy to
    apply deals based on the amount of an
    item present.
    """
    price = 0

    if item in self.pricing:
      # Transform the pricing data so that
      # prices for amounts of items are in
      # descending order
      sorted_prices = dict(
        sorted(self.pricing[item].items(),
               key=lambda item: item[1],
               reverse=True))

      for n in sorted_prices:
        price += (amount // int(n)) * sorted_prices[n]
        amount = amount % int(n)

    return price
