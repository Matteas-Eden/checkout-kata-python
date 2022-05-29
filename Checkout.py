class Checkout:
    def __init__(self, rules):
        self.rules = rules
        self.total = 0
        self.scannedItems = dict()

    def scan(self, item):
        """
        Scan an item into the checkout.
        """
        if item in self.scannedItems:
            self.scannedItems[item] += 1
        else:
            self.scannedItems[item] = 1
        self._updateTotal()

    def _updateTotal(self):
        """
        Based on the scanned items, update the running total
        using the information from the pricing rules.

        Refactor note: Why calculate total from scratch
        each time? If there's a way to only update the total
        based on the most recently scanned item then it
        makes an O(n) algorithm into an O(1) algorithm
        """
        self.total = 0
        for item, amount in self.scannedItems.items():
            price = self.rules.getPrice(item, amount)
            self.total += price
