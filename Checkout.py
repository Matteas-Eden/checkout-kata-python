class Checkout:

  def __init__(self, rules):
    self.rules = rules
    self.total = 0
    self.scannedItems = dict()

  def scan(self, item):
    """
    Scan an item into the checkout.
    """
    name = item.name

    if name in self.scannedItems:
      self.scannedItems[name]['amount'] += 1
    else:
      self.scannedItems[name] = {'amount': 1, 'price': 0}

    amount = self.scannedItems[name]['amount']

    self.scannedItems[item.name]['price'] = self.rules.getPrice(name, amount)

    self._updateTotal()

  def _updateTotal(self):
    """
    Construct an updated total from the currently scanned items.
    """
    self.total = 0

    for item in self.scannedItems.values():
      self.total += item['price']
