import random
import sys

def sample_function_call():
    1 / 0

def group_orders_by_customer(orders):
    customer_totals = {}
    for order in orders:
        customer_id = order.get("customer_id")
        total = order.get("total", 0)
        if customer_id not in customer_totals:
            customer_totals[customer_id] = 0
        customer_totals[customer_id] += total
    return customer_totals

def generate_exceptions():
    my_list = [1, 2, 3]
    print(my_list[5])

def generate_more_exceptions():
    def zero_division(): return 1 / 0
    def index_error(): return [][1]
    def key_error(): return {'a': 1}['b']
    def type_error(): return 'a' + 1
    def value_error(): return int('abcdefgh')
    def file_not_found(): open('nofile.txt')
    def attr_error(): return None.append(1)
    def name_error(): return unknown_var
    def import_error(): import non_existent
    def general_error(): raise Exception("General")
    def custom_error():
        class Custom(Exception): pass
        raise Custom("Custom raised")
    def nested_error(): return [][1][2]
    def gen_error(): (lambda: (_ for _ in ()).throw(RuntimeError("gen error")))()
    def int_type(): return int(None)
    def float_val(): return float('not-a-number')
    def decode_bytes(): bytes.decode(123)
    def format_index(): return '{} {}'[3].format('a', 'b')
    def sqrt_neg(): import math; return math.sqrt(-1)
    def open_proc(): open('/proc/does_not_exist')
    def obj_index(): return object()["not"]

    exception_functions = [
        zero_division, index_error, key_error, type_error, value_error,
        file_not_found, attr_error, name_error, import_error, general_error,
        custom_error, nested_error, gen_error, int_type, float_val,
        decode_bytes, format_index, sqrt_neg, open_proc, obj_index
    ]

    chosen_function = random.choice(exception_functions)

    return chosen_function()
