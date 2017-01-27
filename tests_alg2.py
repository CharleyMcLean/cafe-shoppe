import unittest
import json
import coffee_shop_2


# Load and parse the json file.
# The file name in "" may be changed to test other data sets
test_order_data = []
with open("test_input.json") as json_file:
    # Use a try/except in case the json file is empty
    try:
        json_data = json.load(json_file)
        for order in json_data:
            test_order_data.append(order)
    except:
        test_order_data = []


class TestCase(unittest.TestCase):

    def test_fill_queue1(self):
        test_queues = coffee_shop_2.fill_queue(test_order_data)
        test_tea_queue = test_queues[0]
        first_out = test_tea_queue.dequeue()
        assert first_out == {"order_id": 2,
                             "order_time": 1,
                             "type": "tea"}

    def test_fill_queue2(self):
        test_queues = coffee_shop_2.fill_queue(test_order_data)
        test_affogato_queue = test_queues[1]
        first_out = test_affogato_queue.dequeue()
        assert first_out == {"order_id": 1,
                             "order_time": 0,
                             "type": "affogato"}

    def test_find_brew_time(self):
        assert coffee_shop_2.find_brew_time("latte") == 4

    def test_make_drinks1(self):
        test_queues = coffee_shop_2.fill_queue(test_order_data)
        test_tea_queue = test_queues[0]
        test_drinks_made = coffee_shop_2.make_drinks(test_tea_queue,
                                                     coffee_shop_2.emp1)
        # Below is failing.  Showing 'start_time': 24
        print test_drinks_made[-1]
        assert test_drinks_made[-1] == {'barista_id': 1,
                                        'order_id': 4,
                                        'start_time': 7}

    def test_make_drinks2(self):
        test_queues = coffee_shop_2.fill_queue(test_order_data)
        test_affogato_queue = test_queues[1]
        test_drinks_made = coffee_shop_2.make_drinks(test_affogato_queue,
                                                     coffee_shop_2.emp1)
        print test_drinks_made[-1]
        # Below is failing.  Showing 'start_time': 41
        assert test_drinks_made[-1] == {'barista_id': 2,
                                        'order_id': 1,
                                        'start_time': 0}


if __name__ == "__main__":
    unittest.main()
