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
        """Unittest for filling the tea and latte queue"""
        test_queue1 = coffee_shop_2.Queue()
        test_queue2 = coffee_shop_2.Queue()

        coffee_shop_2.fill_queues(test_order_data, test_queue1, test_queue2)
        first_tea_latte_out = test_queue1.dequeue()
        assert first_tea_latte_out == {"order_id": 2,
                                       "order_time": 1,
                                       "type": "tea"}

    def test_fill_queue2(self):
        """Unittest for filling the affogato queue"""
        test_queue1 = coffee_shop_2.Queue()
        test_queue2 = coffee_shop_2.Queue()

        coffee_shop_2.fill_queues(test_order_data, test_queue1, test_queue2)
        first_affogato_out = test_queue2.dequeue()
        assert first_affogato_out == {"order_id": 1,
                                      "order_time": 0,
                                      "type": "affogato"}

    def test_find_brew_time(self):
        """Unittest for finding the brewtime."""
        assert coffee_shop_2.find_brew_time("latte") == 4

    def test_make_drinks1(self):
        """Unittest for the first employee who is making teas and lattes."""
        test_queue1 = coffee_shop_2.Queue()
        test_queue2 = coffee_shop_2.Queue()
        test_emp3 = coffee_shop_2.Employee(3)

        coffee_shop_2.fill_queues(test_order_data, test_queue1, test_queue2)
        test_drinks_made = coffee_shop_2.make_drinks(test_queue1, test_emp3)

        assert test_drinks_made[-1] == {'barista_id': 3,
                                        'order_id': 4,
                                        'start_time': 7}

    def test_make_drinks2(self):
        """Unittest for the second employee who is making affogatos"""
        test_queue1 = coffee_shop_2.Queue()
        test_queue2 = coffee_shop_2.Queue()
        test_emp4 = coffee_shop_2.Employee(4)

        coffee_shop_2.fill_queues(test_order_data, test_queue1, test_queue2)
        test_drinks_made = coffee_shop_2.make_drinks(test_queue2, test_emp4)

        assert test_drinks_made[-1] == {'barista_id': 4,
                                        'order_id': 1,
                                        'start_time': 0}


if __name__ == "__main__":
    unittest.main()
