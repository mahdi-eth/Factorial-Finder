def factorial(n):
    factorial = 1
    if n == 0: return print(1)
    for i in range(2,n+1):
        x = factorial * i
        factorial = x
    print(factorial)


n = abs(int(input("Enter any number to see it's factorial : ")))
factorial(n)