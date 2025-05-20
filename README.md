# Coffee Shop Challenge

This is a small Python project that models a coffee shop using classes and object-oriented programming.

### What the Project Does

The project includes three main parts:

- **Customer**: Someone who orders coffee.
- **Coffee**: The type of coffee being ordered.
- **Order**: A connection between a customer and a coffee, with a price.

Each customer can make many orders. Each coffee can be ordered by many customers. The `Order` class connects a customer to a coffee and keeps track of how much they paid.

### How It Works

- A customer has a name (between 1 and 15 characters).
- A coffee has a name (at least 3 characters long). Once set, it can't be changed.
- An order connects a customer and a coffee and includes a price (between $1.00 and $10.00).

There are also some helpful methods to get information like:
- All orders a customer has made.
- All coffees a customer has tried.
- How many times a coffee has been ordered.
- The average price paid for a coffee.
- And (bonus) which customer has spent the most on a certain coffee.

### Files and Folders

- `customer.py` – Contains the Customer class.
- `coffee.py` – Contains the Coffee class.
- `order.py` – Contains the Order class.
- `debug.py` – A file where you can test things manually.
- `tests/` – A folder that will hold test files for checking if the code works correctly.

### Why This Project Exists

This project was built to practice using Python classes and object relationships. It focuses on building clear connections between data (like which customer ordered what) and making sure everything is validated properly.

