"""def square(x):

    return x * x#Assigning a function to a variable


f = square
print(f(5))  # Output: 25Passing a function as an argument


def apply_function(func, value):
    return func(value)
result = apply_function(square, 4)
print(result)  # Output: 16"""
# Lambda function to add two numbers

add = lambda a, b: a + b
print(add(3, 5))  # Output: 8Using a lambda function with map


numbers = [1, 2, 3, 4]
squared = map(lambda x: x * x, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

