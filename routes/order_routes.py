from flask import Blueprint, request, jsonify
from models.priority_queue import OrderQueue

order_routes = Blueprint('order_routes', __name__)

order_queue = OrderQueue()

@order_routes.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    customer_name = data.get('customer_name')
    priority = data.get('priority', 5)  # Default priority (Regular customer)
    product_name = data.get('product_name')

    if not customer_name or not product_name:
        return jsonify({"error": "Missing required fields"}), 400

    order_queue.add_order(customer_name, priority, product_name)
    return jsonify({"message": "Order placed successfully!"})

@order_routes.route('/api/process_order', methods=['GET'])
def process_order():
    order = order_queue.process_order()
    if order:
        return jsonify({"message": f"Processing order for {order.customer_name} ({order.product_name})"})
    return jsonify({"message": "No orders in queue"})

@order_routes.route('/api/orders', methods=['GET'])
def get_orders():
    orders = order_queue.get_all_orders()
    order_list = [{"customer_name": order.customer_name, "priority": order.priority, "product_name": order.product_name} for order in orders]
    return jsonify({"orders": order_list})
