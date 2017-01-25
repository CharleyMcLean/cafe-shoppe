from class_defs import Queue, Employee
import json

# Instantiate an instance of the Queue class to represent the coffee queue
coffee_queue = Queue()

# Instantiate two instances of the Employee class to represent the two baristas
emp1 = Employee(1)
emp2 = Employee(2)

TOTAL_TIME = 100

DRINKS = [
    {"type": "tea", "brew_time": 3, "profit": 2},
    {"type": "latte", "brew_time": 4, "profit": 3},
    {"type": "affogato", "brew_time": 7, "profit": 5}
]


def fill_queue(orders_of_the_day):
    """Define a function to fill the queue for the day."""
    for order in orders_of_the_day:
        coffee_queue.enqueue(order)
    return coffee_queue


def make_drinks(coffee_queue):
    """Function to create JSON output representing drinks made for the day.
    Drinks are made first come, first served.  Output includes order_id,
    start_time, and barista_id."""
    drinks_made = []
    # ex: next = {"order_id": 1, "order_time": 0, "type": "affogato"}
    next = coffee_queue.dequeue()

    for i in range(TOTAL_TIME + 1):
        # i is the current time

        if emp1.available and next["order_time"] >= i and emp1.time <= i:
            emp1.available = False

            start_time = 0
            if i > emp1.time:
                start_time = i
            else:
                start_time = emp1.time

            drinks_made.append({"order_id": next["order_id"],
                                "start_time": start_time,
                                "barista_id": emp1.emp_id})
            next_drink = {}
            for drink in DRINKS:
                if next["type"] == drink["type"]:
                    next_drink = drink

            emp1.time += next_drink["brew_time"]
            if not coffee_queue.isEmpty():
                next = coffee_queue.dequeue()

        if emp2.available and next["order_time"] >= i and emp2.time <= i:
            emp2.available = False
            start_time = 0
            if i > emp2.time:
                start_time = i
            else:
                start_time = emp2.time

            drinks_made.append({"order_id": next["order_id"],
                                "start_time": start_time,
                                "barista_id": emp2.emp_id})
            next_drink = {}
            for drink in DRINKS:
                if next["type"] == drink["type"]:
                    next_drink = drink

            emp2.time += next_drink["brew_time"]
            if not coffee_queue.isEmpty():
                next = coffee_queue.dequeue()

        if not emp1.available and emp1.time == i:
            emp1.available = True
        if not emp2.available and emp2.time == i:
            emp2.available = True

    return drinks_made











    # drinks_made = []
    # # ex: next = {"order_id": 1, "order_time": 0, "type": "affogato"}
    # next = coffee_queue.dequeue()
    # for i in range(coffee_queue.size()):
    #     if emp_1.available and next["order_time"] >= emp_1.time:
    #         # Append order info to list of daily orders
    #         emp_1.available = False
    #         drinks_made.append({"order_id": next["order_id"],
    #                             "start_time": emp_1.time,
    #                             "barista_id": emp_1.emp_id})
    #         emp_1.time += next["order_time"]
    #         emp_1.available = True

    #     elif emp_2.available and next["order_time"] >= emp_2.time:
    #         emp_2.available = False
    #         drinks_made.append({"order_id": next["order_id"],
    #                             "start_time": emp_2.time,
    #                             "barista_id": emp_2.emp_id})
    #         emp_2.time += next["order_time"]
    #         emp_2.available = True
    #     next = coffee_queue.dequeue()

    # return drinks_made
