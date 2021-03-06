import unittest
import json
import coffee_shop_1


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

    def test_fill_queue(self):
        """Unittest for fillilng the queue."""
        test_queue = coffee_shop_1.Queue()
        coffee_shop_1.fill_queue(test_order_data, test_queue)
        first_out = test_queue.dequeue()
        assert first_out == {'order_id': 1,
                             'order_time': 0,
                             'type': 'affogato'}

    def test_find_brew_time(self):
        """Unittest for determining brewtime"""
        assert coffee_shop_1.find_brew_time("tea") == 3

    def test_make_drinks(self):
        """Unittest for the drinks made."""
        test_queue = coffee_shop_1.Queue()
        test_emp3 = coffee_shop_1.Employee(3)
        test_emp4 = coffee_shop_1.Employee(4)

        coffee_shop_1.fill_queue(test_order_data, test_queue)
        test_drinks_made = coffee_shop_1.make_drinks(test_queue, test_emp3, test_emp4)
        print test_drinks_made
        # The below is failing.  Showing 'start_time': 11
        assert test_drinks_made[-1] == {'barista_id': 3,
                                        'order_id': 4,
                                        'start_time': 7}


if __name__ == "__main__":
    unittest.main()
