#Use of default parameters
def greet(name, greeting="Hello"):
    """
    Greets a person with a specified greeting (default is "Hello").
    """
    print(greeting,name)

# Using the function with both arguments provided
greet("Alice", "Hi")

# Using the function with only the 'name' argument, 'greeting' defaults to "Hello"
greet("Bob")

# Using the function with both arguments provided again
greet("Charlie", "Hey")