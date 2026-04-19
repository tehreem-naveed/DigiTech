#Task2: odd, even and prime numbers
#This code take 10 number and then categorizes them using functions
def odds(n):
    odds = []
    for num in n:
        if num % 2 != 0:
            odds.append(num)
    return odds
def evens(n):
    evens = []
    for num in n:
        if num % 2 == 0:
            evens.append(num)
    return evens
def primes(n):
    primes = []
    for num in n:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

n = []
for i in range(1, 11):
    value = int(input(f"Enter number {i}: "))
    n.append(value)
odds = odds(n)
evens = evens(n)
primes = primes(n)
print("\nOdd Numbers:", odds if odds else "None found")
print("Even Numbers:", evens if evens else "None found")
print("Prime Numbers:", primes if primes else "None found")