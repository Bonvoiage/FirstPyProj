def calculate_order_sum(items):
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total

def calculate_tax(amount, tax_rate):
    return amount * tax_rate

def calculate_shipping(weight):
    base_rate = 5
    rate_per_kg = 2
    return base_rate + rate_per_kg * weight

def calculate_total_order(items, tax_rate, weight):
    order_sum = calculate_order_sum(items)
    tax = calculate_tax(order_sum, tax_rate)
    shipping = calculate_shipping(weight)
    return order_sum + tax + shipping


items = [
    {'price': 10, 'quantity': 2},  # Пример товара: цена 10, количество 2
    {'price': 5, 'quantity': 2},
    {'price': 2, 'quantity': 5}]
tax_rate = 0.1  # 10% налог
weight = 5  # Общий вес заказа

items2 = [
    {'price': 20, 'quantity': 1},  # Пример товара: цена 10, количество 2
    {'price': 10, 'quantity': 1},
    {'price': 10, 'quantity': 1}]

total_cost = calculate_total_order(items, tax_rate, weight)
print(f"price для игрушек: {calculate_order_sum(items)}")
# print(total_cost)  
