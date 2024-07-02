def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print(f"Add: 1 + 2 = {add(1, 2)}")
    print(f"Subtract: 5 - 3 = {subtract(5, 3)}")
    print(f"Multiply: 4 * 2 = {multiply(4, 2)}")
    print(f"Divide: 8 / 4 = {divide(8, 4)}")