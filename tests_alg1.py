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
        test_queue = coffee_shop_1.fill_queue(test_order_data)
        first_out = test_queue.dequeue()
        assert first_out == {"order_id": 1, "order_time": 0, "type": "affogato"}


if __name__ == "__main__":
    unittest.main()
