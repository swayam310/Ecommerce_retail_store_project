from flask import Blueprint, request, jsonify
from models.trie import Trie
from models.merge_sort import merge_sort

product_routes = Blueprint('product_routes', __name__)

# Sample product list with price and popularity
products = [
    {"name": "apple", "price": 100, "popularity": 5},
    {"name": "banana", "price": 50, "popularity": 7},
    {"name": "orange", "price": 80, "popularity": 6},
    {"name": "grape", "price": 120, "popularity": 4},
    {"name": "mango", "price": 150, "popularity": 9},
    {"name": "blueberry", "price": 200, "popularity": 8},
]

# Initialize Trie and insert products
trie = Trie()
for product in products:
    trie.insert(product["name"])

@product_routes.route('/api/search', methods=['GET'])
def search_products():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify({"error": "No search query provided"}), 400
    results = trie.search_prefix(query)
    return jsonify({"suggestions": results})

@product_routes.route('/api/products', methods=['GET'])
def get_products():
    sort_by = request.args.get('sort_by', 'price')  # Default sort by price
    if sort_by not in ["price", "popularity"]:
        return jsonify({"error": "Invalid sort parameter"}), 400
    
    sorted_products = merge_sort(products, sort_by)
    return jsonify({"products": sorted_products})
