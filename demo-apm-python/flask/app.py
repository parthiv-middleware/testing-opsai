from flask import Flask

import logging
import sys
from test import sample_function_call
from test import group_orders_by_customer
from test import generate_exceptions
from test import generate_more_exceptions
logging.getLogger().setLevel(logging.INFO)
logging.info("Application initiated successfully.", extra={'Tester': 'Alex'})

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.error("error log sample", extra={'CalledFunc': 'hello_world'})
    logging.warning("warning log sample")
    logging.info("info log sample")
    return 'Hello World!'

@app.route('/exception1')
def sample_function():
    sample_function_call()

@app.route('/exception2')
def order_listing():
    orders = [
        {"customer_id": "C001", "total": 120.50},
        {"customer_id": "C002", "total": 75.00},
        {"customer_id": "C001", "total": 30.00},
        {"customer_id": "C003", "total": 99.99},
        {"customer_id": "C002", "total": 25.00},
    ]
    group_orders_by_customer(orders)


@app.route('/exception3')
def generate_exception():
    generate_exceptions()

@app.route('/exception4')
def generate_more_exception():
    generate_more_exceptions()

if __name__ == '__main__':
    app.run('0.0.0.0', 8010)