price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95, 'pomegranate': 4.95}

quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1, 'pomegranate': 2}

# Function to calculate the total cost of all fruits purchased
def total_cost_shopping():
    total_cost = 0
    for fruit in price_list.keys():
        if fruit in quantity_list:
            total_cost += price_list[fruit] * quantity_list[fruit]
    print("Total cost = ", total_cost)

# Function to calculate the cost of a specific fruit and its quantity
def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity * price_list[key]
            break
    print("Cost of ", quantity, fruit, "=", cost)

# Main function to test the other functions
def main():
    cost_of_fruits('apple', 10)  # Test with apple and quantity 10
    total_cost_shopping()  # Calculate total cost of shopping

if __name__ == "__main__":
    main()
