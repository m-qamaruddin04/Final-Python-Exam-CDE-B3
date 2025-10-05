def perform_operations(numbers):
    total = 0
    product = 1

    for num in numbers:
        total += num       # Add each number to total
        product *= num     # Multiply each number for product

    average = total / len(numbers)
    return total, product, average


# Test the function
numbers = [1, 2, 3, 4, 5]
total, product, average = perform_operations(numbers)

print("Total:", total)
print("Product:", product)
print("Average:", average)
