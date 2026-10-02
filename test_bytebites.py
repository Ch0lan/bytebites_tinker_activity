import pytest

from models import Customer, Menu, MenuItem, Order


@pytest.fixture
def burger():
    return MenuItem("Spicy Burger", 10.00, "Burgers", 4.7)


@pytest.fixture
def soda():
    return MenuItem("Large Soda", 5.00, "Drinks", 4.1)


@pytest.fixture
def menu(burger, soda):
    m = Menu()
    m.add_item(burger)
    m.add_item(soda)
    m.add_item(MenuItem("Iced Tea", 2.50, "Drinks", 3.8))
    m.add_item(MenuItem("Choc Cookie", 1.75, "Desserts", 4.9))
    return m


# --- Order totals ---------------------------------------------------------

def test_calculate_total_with_multiple_items(burger, soda):
    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    assert order.calculate_total() == 15.00


def test_order_total_is_zero_when_empty():
    assert Order().calculate_total() == 0


def test_order_total_counts_duplicate_items(soda):
    order = Order()
    order.add_item(soda)
    order.add_item(soda)
    assert order.calculate_total() == 10.00


def test_order_total_rounds_to_cents():
    order = Order()
    order.add_item(MenuItem("A", 0.10, "Snacks", 1))
    order.add_item(MenuItem("B", 0.20, "Snacks", 1))
    assert order.calculate_total() == 0.30


# --- Menu filtering -------------------------------------------------------

def test_filter_by_category_returns_only_matching_items(menu):
    drinks = menu.filter_by_category("Drinks")
    assert [i.name for i in drinks] == ["Large Soda", "Iced Tea"]


def test_filter_by_category_ignores_case_and_whitespace(menu):
    assert len(menu.filter_by_category("  dRiNkS ")) == 2


def test_filter_by_unknown_category_returns_empty_list(menu):
    assert menu.filter_by_category("Soup") == []


def test_filter_does_not_change_the_menu(menu):
    menu.filter_by_category("Drinks")
    assert len(menu.items) == 4


# --- Menu sorting ---------------------------------------------------------

def test_sort_by_popularity_puts_most_popular_first(menu):
    names = [i.name for i in menu.sort_by_popularity()]
    assert names == ["Choc Cookie", "Spicy Burger", "Large Soda", "Iced Tea"]


def test_sort_by_price_puts_cheapest_first(menu):
    names = [i.name for i in menu.sort_by_price()]
    assert names == ["Choc Cookie", "Iced Tea", "Large Soda", "Spicy Burger"]


def test_sorting_does_not_reorder_the_menu(menu):
    before = list(menu.items)
    menu.sort_by_price()
    menu.sort_by_popularity()
    assert menu.items == before


def test_sort_empty_menu_returns_empty_list():
    assert Menu().sort_by_price() == []


# --- MenuItem validation --------------------------------------------------

def test_menu_item_stores_its_attributes(burger):
    assert (burger.name, burger.price, burger.category, burger.popularity) == (
        "Spicy Burger", 10.00, "Burgers", 4.7)


def test_menu_item_rejects_negative_price():
    with pytest.raises(ValueError):
        MenuItem("Free Lunch", -1, "Burgers", 3)


def test_menu_item_rejects_blank_name():
    with pytest.raises(ValueError):
        MenuItem("   ", 1, "Burgers", 3)


# --- Customer -------------------------------------------------------------

def test_new_customer_is_not_verified():
    assert Customer("Alice").is_verified() is False


def test_customer_with_past_order_is_verified(burger):
    order = Order()
    order.add_item(burger)
    alice = Customer("Alice")
    alice.add_purchase(order)
    assert alice.is_verified() is True


def test_customer_with_blank_name_is_not_verified(burger):
    order = Order()
    order.add_item(burger)
    ghost = Customer("  ")
    ghost.add_purchase(order)
    assert ghost.is_verified() is False
