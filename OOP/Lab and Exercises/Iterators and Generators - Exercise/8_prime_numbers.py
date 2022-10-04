
# Create a generator function called get_primes() which should receive a list of integer numbers and return a list containing only the prime numbers from the initial list. 
# You can learn more about prime numbers from here

def get_primes(num_list: list) -> iter:
    def is_prime(num: int) -> bool:
        if num > 1:
            if any(num % x == 0 for x in range(2, (num + 1) // 2 + 1)):
                return False
            return True
        return False

    for el in num_list:
        if isinstance(el, int):
            if is_prime(el):
                yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
