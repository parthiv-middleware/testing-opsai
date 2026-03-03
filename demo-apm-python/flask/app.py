from flask import Flask, jsonify
from test import sample_function_call, group_orders_by_customer, generate_exceptions, generate_more_exceptions
from middleware import MwTracker

app = Flask(__name__)

tracker = MwTracker()
tracker.track()

@app.route('/')
def hello_world():
    app.logger.debug('this is a DEBUG message')
    app.logger.info('this is an INFO message')
    app.logger.warning('this is a WARNING message')
    app.logger.error('this is an ERROR message')
    app.logger.critical('this is a CRITICAL message')
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
    result = group_orders_by_customer(orders)
    return jsonify(result)

@app.route('/exception3')
def generate_exception():
    generate_exceptions()

@app.route('/exception4')
def generate_more_exception():
    generate_more_exceptions()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)