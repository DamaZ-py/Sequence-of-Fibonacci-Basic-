# Declaring the role
def fib(n):

    a, b = 0,1 # Simultaneously declaring the variable
    
    while a < n: # Verification loop 
        print(a, end="... " )
        a, b = b, a+b # If not "b" then "a+b"

    print()

fib(100)
