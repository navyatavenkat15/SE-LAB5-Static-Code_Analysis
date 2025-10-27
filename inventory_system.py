'''Inventory Management System'''
import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    ''' Add an item to inventory and increase its quantity'''
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid item name or quantity type.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    '''Remove the required item and decrease its quantity'''
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    '''Print quantity of a particular item'''
    return stock_data[item]


def load_data(file="inventory.json"):
    '''Loading the json file'''
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    stock_data.update(data)


def save_data(file="inventory.json"):
    '''Saving the json file with changes'''
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    '''Printing a report of the inventory'''
    print("Items Report")
    for item, qty in stock_data.items():
        print(item, "->", qty)


def check_low_items(threshold=5):
    '''Checking which items are below threshold and displaying them'''
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)

    return result


def main():
    '''Main Function'''
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("demo completed")


main()
