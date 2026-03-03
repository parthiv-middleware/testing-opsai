from flask import Flask, jsonify, request
from test import divide, group_orders_by_customer
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask APM Demo!"

@app.route('/divide')
def divide_route():
    try:
        numerator = float(request.args.get('numerator', 10))
        denominator = float(request.args.get('denominator', 0))
        result = divide(numerator, denominator)
        return jsonify({"result": result})
    except ZeroDivisionError as e:
        return jsonify({"error": str(e)}), 400
    except ValueError as e:
        return jsonify({"error": "Invalid input: Please provide numeric values"}), 400

@app.route('/exception1')
def exception_route():
    result = divide(10, 0)
    return jsonify({"result": result})

@app.route('/exception2')
def order_listing():
    orders = [
        {"customer_id": "C001", "total": 120.50},
        {"customer_id": "C002", "total": 75.00},
        {"customer_id": "C001", "total": 30.00},
        {"customer_id": "C003", "total": 99.99},
        {"customer_id": "C002", "total": 25.00},
    ]
    customer_totals = group_orders_by_customer(orders)
    return jsonify(customer_totals)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)