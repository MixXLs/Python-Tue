def fibonacci(n):
    if n == 0:
        return 0 #Base case
    elif n == 1:
        return 1 #Base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) #Recursive case
    
print(fibonacci(6))