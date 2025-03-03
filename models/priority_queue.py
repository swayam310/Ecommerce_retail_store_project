import heapq

class Order:
    def __init__(self, customer_name, priority, product_name):
        self.customer_name = customer_name
        self.priority = priority  # Lower value = Higher priority (VIP customers)
        self.product_name = product_name

    def __lt__(self, other):
        return self.priority < other.priority

class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, customer_name, priority, product_name):
        heapq.heappush(self.queue, Order(customer_name, priority, product_name))

    def process_order(self):
        if self.queue:
            return heapq.heappop(self.queue)
        return None

    def get_all_orders(self):
        return sorted(self.queue, key=lambda x: x.priority)  # Sorted by priority
