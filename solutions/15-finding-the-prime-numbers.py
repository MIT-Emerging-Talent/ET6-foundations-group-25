"""
A module for generating prime numbers up to a given limit.

Module contents:
    - generate_primes(limit): Generates a list of prime numbers up to a given limit.
    - get_valid_input(prompt): Prompts the user for valid input and validates it as a positive number.

Prime number generation rules:
    - A prime number is a natural number greater than 1 that is not divisible by any number other than 1 and itself.
"""


def generate_primes(limit):
    """
    Generate a series of prime numbers up to a given limit.

    Args:
        limit (float): The upper limit up to which prime numbers are generated.

    Returns:
        list: A list of prime numbers up to the specified limit.

    Raises:
        AssertionError:
            - If 'limit' is not a float or integer.
            - If 'limit' is less than 2.

    Example:
        >>> generate_primes(10)
        [2, 3, 5, 7]
    """
    # Input validation
    assert isinstance(limit, (int, float)), "Limit must be a float or an integer"
    assert limit >= 2, "Limit must be greater than or equal to 2"

    primes = []
    for num in range(2, int(limit) + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes


def get_valid_input(prompt):
    """
    Prompt the user for input and validate it as a positive number (integer or float).

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        float: A valid positive number input.

    Raises:
        AssertionError: If the prompt is not a string.

    Example:
        >>> get_valid_input("Enter a number: ")
        # User enters 10
        10.0
    """
    assert isinstance(prompt, str), "Prompt must be a string"

    while True:
        try:
            value = float(input(prompt))  # Accept input as float
            if value > 0:  # Ensure the value is positive
                return value
            print("The number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    user_limit = get_valid_input("Enter the limit for prime numbers: ")
    print(f"Prime numbers up to {int(user_limit)}: {generate_primes(user_limit)}")
