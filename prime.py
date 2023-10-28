import math

def is_prime(n):
    """
    Check if a number is a prime number.

    Args:
    n (int): The number to be checked for primality.

    Returns:
    bool: Returns True if the number is a prime number, False otherwise.

    Examples:
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
