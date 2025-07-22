def factorial(n): #factorial การคูณ 5*4*3*2*1
    if n == 0:
        return 1 #Base case
    else:
        return n * factorial(n - 1) #Recursive case
    
print(factorial(5))