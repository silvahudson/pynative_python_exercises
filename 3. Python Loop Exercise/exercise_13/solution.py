def factorial(n):
    factorial = 1
    if n == 0 or n ==1:
        return(factorial)
    else:
        for i in range(n, 0, -1):
            factorial *= i 
        return factorial

if __name__ == "__main__":
    n = 5
    print(factorial(n))
    
    