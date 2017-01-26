from class_defs import Queue, Employee
import json


# Instantiate two instances of the Employee class to represent the two baristas
emp1 = Employee(1)
emp2 = Employee(2)

# Global variable to hold drink types and their characteristics
DRINKS = [
    {"type": "tea", "brew_time": 3, "profit": 2},
    {"type": "latte", "brew_time": 4, "profit": 3},
    {"type": "affogato", "brew_time": 7, "profit": 5}
]


# Load and parse the json file.
# The file name in "" may be changed to test other data sets
order_data = []
with open("input.json") as json_file:
    # Use a try/except in case the json file is empty
    try:
        json_data = json.load(json_file)
        for order in json_data:
            order_data.append(order)
    except:
        order_data = []


# Instantiate two instances of the Queue class to represent the coffee queues.
# One queue will hold tea and latte orders, and the other will hold affogatos.
# One employee will be assigned to each line.
tea_latte_queue = Queue()
affogato_queue = Queue()


def fill_queue(orders_of_the_day):
    """Define a function to fill the queues with the orders of the day."""
    for order in orders_of_the_day:
        if order["type"] == "affogato":
            affogato_queue.enqueue(order)
        else:
            tea_latte_queue.enqueue(order)
    return tea_latte_queue, affogato_queue


def make_drinks(coffee_queue, emp):
    """Function to create JSON output representing drinks made for the day.
    Drinks are made first come, first served.  Output includes order_id,
    start_time, and barista_id."""
    # drinks_made = []
    # ex: next = {"order_id": 1, "order_time": 0, "type": "affogato"}
    next = {}
    time_counter = 0
    drinks_made = []
    if coffee_queue.isEmpty():
        return drinks_made
    if not coffee_queue.isEmpty():
        next = coffee_queue.dequeue()

    while time_counter < 101:
        if emp.time_avail <= time_counter:
            # if the order is placed after the employee becomes available
            # the start time will be when the order is placed
            if next["order_time"] > emp.time_avail:
                start_time = next["order_time"]
            else:
                start_time = emp.time_avail

            drinks_made.append({"order_id": next["order_id"],
                                "start_time": start_time,
                                "barista_id": emp.emp_id})

            brew_time = find_brew_time(next["type"])
            emp.time_avail += brew_time

            if coffee_queue.isEmpty():
                break
            else:
                next = coffee_queue.dequeue()

        time_counter += 1

    return drinks_made


def find_brew_time(order_type):
    """Helper function to determine brew time"""
    brew_time = int()
    for drink in DRINKS:
        if order_type == drink["type"]:
            brew_time = drink["brew_time"]

    return brew_time


#####################################################################
# Fill queue with orders of the day, and generate output data.
fill_queue(order_data)
emp1_orders_made = make_drinks(tea_latte_queue, emp1)
emp2_orders_made = make_drinks(affogato_queue, emp2)

print "Employee 1 made the following tea and latte orders:", emp1_orders_made
print "Employee 2 made the following tea and latte orders:", emp2_orders_made
