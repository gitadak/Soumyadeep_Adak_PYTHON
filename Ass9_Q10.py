#Use of variable length argument
def sum_all(*args):
    """
    Calculates the sum of all the provided arguments.
    """
    total = 0
    for num in args:
        total += num
    return total

# Call the function with different numbers of arguments
result1 = sum_all(1, 2, 3, 4, 5)
result2 = sum_all(10, 20, 30)
result3 = sum_all()

# Print the results
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)