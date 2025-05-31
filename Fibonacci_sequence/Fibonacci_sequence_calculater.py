from decimal import Decimal, getcontext
from os import system

#Set precision
getcontext().prec = 5000

#golden ratio definition
sqrt_5 = Decimal(5).sqrt()
phi = (Decimal(1) + sqrt_5) / Decimal(2)

#Fibonacci sequence calculate
def fibonacci_binet(n):
    term1 = phi ** n
    term2 = (1 - phi) ** n
    fib_n = (term1 - term2) / sqrt_5
    return int(fib_n.to_integral_value(rounding='ROUND_HALF_EVEN'))

#input last Fibonacci sequence
try:
    loop = int(input("Please write number of last Fibonacci sequence(-1 => infinite): "))
except ValueError:
    print("The input value is not an integer.")
    exit()
with open(f"Fibonacci_sequence/Fibonacci_sequence_until_{loop}","w") as file:
    if loop == -1:
        i = 1
        while True:
            system('cls')
            file.write(f"F({i})={fibonacci_binet(i)}\n")
            print(f"F({i})={fibonacci_binet(i)}")
            i += 1
    else:
        for i in range(1, loop+1):
            system('cls')
            file.write(f"F({i})={fibonacci_binet(i)}\n")
            print(f"F({i})={fibonacci_binet(i)}")
            i += 1