from app import addition

def main():
    import sys
    num1, num2 = sys.args[1:]
    num1, num2 = int(num1), int(num2)
    result = multiply(num1, num2)
    print(f"Result: {result}")



def multiply(num1, num2):
    total = 0
    for num in range(num2):
        total = addition(total, num1)
    return total


