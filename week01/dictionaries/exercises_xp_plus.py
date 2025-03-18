#exercise 1
# Initial Data
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# Step 1: Calculate the average grade for each student
student_averages = {student: sum(grades) / len(grades) for student, grades in student_grades.items()}

# Step 2: Assign letter grades
def assign_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

student_letter_grades = {student: assign_letter_grade(avg) for student, avg in student_averages.items()}

# Step 3: Calculate class average
class_average = sum(student_averages.values()) / len(student_averages)

# Step 4: Print the results
print("Student Grade Summary:")
for student in student_grades:
    print(f"{student}: Average = {student_averages[student]:.2f}, Grade = {student_letter_grades[student]}")

print(f"\nClass Average: {class_average:.2f}")

#exercise 2
# Initial Data
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# Step 1: Total Sales Calculation
total_sales = {}
for transaction in sales_data:
    product = transaction["product"]
    total_price = transaction["price"] * transaction["quantity"]
    total_sales[product] = total_sales.get(product, 0) + total_price

# Step 2: Customer Spending Profile
customer_spending = {}
for transaction in sales_data:
    customer_id = transaction["customer_id"]
    total_price = transaction["price"] * transaction["quantity"]
    customer_spending[customer_id] = customer_spending.get(customer_id, 0) + total_price

# Step 3: Sales Data Enhancement (Adding "total_price" field)
for transaction in sales_data:
    transaction["total_price"] = transaction["price"] * transaction["quantity"]

# Step 4: High-Value Transactions (Filtering & Sorting)
high_value_transactions = sorted(
    [transaction for transaction in sales_data if transaction["total_price"] > 500],
    key=lambda x: x["total_price"],
    reverse=True
)

# Step 5: Customer Loyalty Identification (Customers with multiple purchases)
purchase_counts = {}
for transaction in sales_data:
    customer_id = transaction["customer_id"]
    purchase_counts[customer_id] = purchase_counts.get(customer_id, 0) + 1

loyal_customers = [customer_id for customer_id, count in purchase_counts.items() if count > 1]

# Bonus: Insights and Analysis

# Average transaction value for each product category
average_transaction_value = {
    product: total_sales[product] / sum(t["quantity"] for t in sales_data if t["product"] == product)
    for product in total_sales.keys()
}

# Identifying the most popular product based on quantity sold
product_quantities = {}
for transaction in sales_data:
    product = transaction["product"]
    product_quantities[product] = product_quantities.get(product, 0) + transaction["quantity"]

most_popular_product = max(product_quantities, key=product_quantities.get)

# Display Results
print("Total Sales:", total_sales)
print("Customer Spending:", customer_spending)
print("High-Value Transactions:", high_value_transactions)
print("Loyal Customers:", loyal_customers)
print("Average Transaction Value:", average_transaction_value)
print("Most Popular Product:", most_popular_product)

# Insights:
"""
1. The most expensive products generate higher total revenue, but headphones are the most popular based on quantity.
2. Customer loyalty can be leveraged with personalized discounts or exclusive deals.
3. Marketing strategies should focus on promoting high-selling items while boosting premium product sales with upsell techniques.
"""
