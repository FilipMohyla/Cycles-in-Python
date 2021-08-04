### Task: Get input (n) from user and count factorial n, figure out if n is prime number 
# and make fibbonacci sequence up to number n ###

from math import factorial
numb = int(input("Zadej číslo: "))
fact_numb = factorial(numb)
rest = []
fibbo_seq = [1, 1]


for sequence in range(2, numb):

    rest.append(numb % sequence)

if 0 in rest:
    primenumb = "není prvočíslo"
if 0 not in rest and numb % numb == 0 and numb % 1 == 0:
    primenumb = "je prvočíslo"


while True:

    if numb == 1:
        fibbo_seq = [1]
        break

    elif (fibbo_seq[-1] + fibbo_seq[-2]) < numb:
        fibbo_seq.append((fibbo_seq[-1] + fibbo_seq[-2]))
    
    else:
        break

print(f"""
Zvolil/a sis číslo {numb}
Faktoriál čísla {numb}: {fact_numb}
Číslo {numb} {primenumb}
Fibonacciho posloupnost až do čísla {numb}: {fibbo_seq} """)