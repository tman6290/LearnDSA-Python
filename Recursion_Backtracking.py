# Recursion

def fact(n:int):
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1

print(fact(5))

#Fibonacci

def fib(n:int):
    if n >= 3:
       return fib(n-1) + fib(n-2)
    else:
        return 1
        

print(fib(6))

#frog problem

def numWays(distance:int):
    if distance <= 1:
        return 1
    else:
        return numWays(distance-1) + numWays(distance - 2)

print(numWays(11))