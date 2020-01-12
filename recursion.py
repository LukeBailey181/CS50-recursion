#factorials worked out using recursion

def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n-1)

number = input("Input Number: ")

print(factorial(number))
