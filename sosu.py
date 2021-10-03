import math

N = 30000


def is_prime(number):
    stop_number = int(math.sqrt(number))
    for i in range(2, stop_number + 1):
        if number % i == 0:
            return False
    return True


def make_prime_list(number, prime_list):
    for prime_number in prime_list:
        if number % prime_number == 0:
            return prime_list
    return prime_list + [number]


prime_list = [2]
number = 2
while N > prime_list[-1]:
    number += 1
    prime_list = make_prime_list(number, prime_list)

print(prime_list[-1])
