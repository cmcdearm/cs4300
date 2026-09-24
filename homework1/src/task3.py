def classify_number(n):
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        # If divisor divides number evenly, return False
        if number % divisor == 0:
            return False
    return True


def print_first_ten_primes():
    found = 0

    for candidate in range(2, 100):
        if is_prime(candidate):
            print(candidate)
            found += 1
            if found == 10:
                break


def sum_one_to_hundred():
    number = 1
    total = 0

    while number <= 100:
        total += number
        number += 1
    return total