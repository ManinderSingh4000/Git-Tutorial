## Find Factorial of a Number
import time
def fact(n ,d):
    if n in d:
        return d[n]
    else:
        d[n]= n * fact(n-1 , d)
    return d[n] 

d= {0: 1, 1: 1} 
start = time.time()  # Start time measurement
factorial = fact(15, d)
time_taken = time.time()  # End time measurement
print(f"Time taken: {time_taken - start} seconds")
print(factorial)  