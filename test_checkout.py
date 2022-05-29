import pytest

from Checkout import Checkout
from Rules import Rules
from Item import Item


@pytest.fixture
def data():
  pytest.rules = Rules()


def test_checkout_empty(data):
  checkout = Checkout(pytest.rules)
  expectedTotal = 0
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_single_item(data):
  checkout = Checkout(pytest.rules)
  item = Item('Apple')
  checkout.scan(item)
  expectedTotal = 50
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_single_deal(data):
  checkout = Checkout(pytest.rules)
  item = Item('Apple')
  checkout.scan(item)
  checkout.scan(item)
  checkout.scan(item)
  expectedTotal = 130
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_different_items(data):
  checkout = Checkout(pytest.rules)
  itemA = Item('Apple')
  itemB = Item('Banana')
  checkout.scan(itemA)
  checkout.scan(itemB)
  checkout.scan(itemA)
  expectedTotal = 130
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_different_items_with_single_deal(data):
  checkout = Checkout(pytest.rules)
  itemA = Item('Apple')
  itemB = Item('Banana')
  checkout.scan(itemA)
  checkout.scan(itemB)
  checkout.scan(itemA)
  checkout.scan(itemB)
  expectedTotal = 145
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_different_items_with_multiple_deals(data):
  checkout = Checkout(pytest.rules)
  itemA = Item('Apple')
  itemB = Item('Banana')

  checkout.scan(itemA)
  checkout.scan(itemA)
  checkout.scan(itemB)
  expectedTotal = 130
  actualTotal = checkout.total
  assert expectedTotal == actualTotal

  checkout.scan(itemA)
  expectedTotal = 160
  actualTotal = checkout.total
  assert expectedTotal == actualTotal

  checkout.scan(itemB)
  expectedTotal = 175
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_accurate_running_total(data):
  checkout = Checkout(pytest.rules)
  itemA = Item('Apple')
  itemB = Item('Banana')
  checkout.scan(itemA)
  checkout.scan(itemB)

  expectedTotal = 80
  actualTotal = checkout.total
  assert expectedTotal == actualTotal

  checkout.scan(itemA)
  expectedTotal = 130
  actualTotal = checkout.total
  assert expectedTotal == actualTotal

  checkout.scan(itemB)
  expectedTotal = 145
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_many_items(data):
  checkout = Checkout(pytest.rules)
  itemA = Item('Apple')
  itemB = Item('Banana')
  itemC = Item('Cheese')
  itemD = Item('Donut')

  checkout.scan(itemA)
  checkout.scan(itemB)
  checkout.scan(itemC)
  checkout.scan(itemD)

  expectedTotal = 115
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_many_items_with_one_deal(data):
  checkout = Checkout(pytest.rules)
  itemA = Item('Apple')
  itemB = Item('Banana')
  itemC = Item('Cheese')
  itemD = Item('Donut')

  checkout.scan(itemA)
  checkout.scan(itemB)
  checkout.scan(itemC)
  checkout.scan(itemD)
  checkout.scan(itemA)
  checkout.scan(itemB)

  expectedTotal = 180
  actualTotal = checkout.total
  assert expectedTotal == actualTotal


def test_checkout_many_items_with_multiple_deals(data):
  checkout = Checkout(pytest.rules)
  itemA = Item('Apple')
  itemB = Item('Banana')
  itemC = Item('Cheese')
  itemD = Item('Donut')

  checkout.scan(itemA)
  checkout.scan(itemB)
  checkout.scan(itemC)
  checkout.scan(itemD)
  checkout.scan(itemA)
  checkout.scan(itemB)
  checkout.scan(itemA)

  expectedTotal = 210
  actualTotal = checkout.total
  assert expectedTotal == actualTotal
