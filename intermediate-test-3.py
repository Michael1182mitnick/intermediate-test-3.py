# Write a program to find all prime factors of a given number.

def prime_factors(n):
    factors = []

    # Divide out the number 2 to handle even numbers first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Now n must be odd, we start checking from 3
    for i in range(3, int(n**0.5) + 1, 2):
        # While i divides n, add i and divide n
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is still greater than 2, it must be prime
    if n > 2:
        factors.append(n)

    return factors


# Example usage
number = int(input("Enter a number: "))
result = prime_factors(number)
print(f"The prime factors of {number} are: {result}")
