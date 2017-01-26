# Cafe Shoppe

There are exactly 2 baristas, with ID numbers ```[1, 2]```. A barista can make at most 1 drink at a time. For example, if a barista starts making a ```3-minute tea``` at ```time=5```, she will deliver the drink at ```time=8``` and can start making a new drink at ```time=8```.

The work day starts at ```time=0``` and ends at ```time=100```.

There are three types of drinks, each of which takes a different amount of time to make and yields a different profit.

```
[
    { "type": "tea",      "brew_time": 3, "profit": 2 },
    { "type": "latte",    "brew_time": 4, "profit": 3 },
    { "type": "affogato", "brew_time": 7, "profit": 5 }
]
```

##Contents
* [Technologies](#technologies)
* [Example Input/Output of the Program](#example_in_and_out)
* [Deliverables](#deliverables)
* [Explanation of Second Algorithm](#explanation)
* [Installation](#install)

## <a name="technologies"></a>Technologies

Tech Stack: Python with json library<br/>


## <a name="example_in_and_out"></a>Example Input/Output of the Program

Below is example input data of orders made in a given day, ordered by ```order_time```. See file ```input.json``` for a full list.

```
[
    { "order_id": 1, "order_time": 0, "type": "affogato" },
    { "order_id": 2, "order_time": 1, "type": "tea" },
    { "order_id": 3, "order_time": 2, "type": "latte" },
    { "order_id": 4, "order_time": 2, "type": "tea" }
]
```

Below is example output data. See file ```output_fifo.json``` for the expected output given ```input.json```. The output of the solutions should include drinks that each barista makes and the time that the barista starts making the drink. It must be valid json - an array of objects with the following format:

```
[
    { "order_id": 1, "start_time": 0, "barista_id": 1 },
    { "order_id": 2, "start_time": 1, "barista_id": 2 },
    { "order_id": 3, "start_time": 4, "barista_id": 2 },
    { "order_id": 4, "start_time": 7, "barista_id": 1 }
]
```


## <a name="deliverables"></a>Deliverables

Design 2 solutions that handle the drink orders. The first is a simple first-in-first-out (FIFO) solution, the second is an algorithm of your choice.

1. Implement a FIFO (first-in-first-out) solution where a drink is immediately assigned to the first available barista. The output must match the json output in ```output_fifo.json``` (spacing doesn't matter). The drink orders are in ```input.json```.

2. Implement a second algorithm that would make the Cafe Shoppe more successful. Use creativity to optimize for a business need. Examples of things to think about: # of drinks made (throughput), shortest average customer wait time, most profit made, etc. Document your reasoning in your README.

**Caveat**:

* not all drinks will necessarily be completed
* for the FIFO solution, all orders processed before or at time=100 will be delivered to the customer, even if the drinks are delivered after time=100.


## <a name="explanation"></a>Explanation of Second Algorithm

Because the time to make one tea and one latte is the same as the time to make one affogato, orders are split into two queues, each assigned to one of the two employees.  Therefore, one employee makes all of the teas and lattes, and one employee makes all the affogatos.  After the orders are split based on type, the orders are made on a FIFO basis.

The first algorithm resulted in 42 orders being completed, while the second algorithm resulted in 44 orders being completed. 


## <a name="install"></a>Installation

To run Cafe Shoppe:

Clone or fork this repo:

```
https://github.com/CharleyMcLean/cafe-shoppe.git
```

Create and activate a virtual environment inside your Cafe Shoppe directory:

```
virtualenv env
source env/bin/activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the file with the algorithm you'd like to test:

```
python coffee_shop_1.py
```

**or**

```
python coffee_shop_.py
```

The orders output will print to the terminal.
