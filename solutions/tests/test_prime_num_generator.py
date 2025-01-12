"""
This module contains unit tests for the max_integer function.
It tests various scenarios including ordered and unordered lists,
lists with floats, strings, and edge cases.
"""

import unittest


def generate_primes(limit):
    """Generate a list of prime numbers up to the given limit."""

    if not isinstance(limit, int) or limit < 2:
        raise AssertionError("Limit must be an integer greater than or equal to 2.")

    primes = []

    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))

        if is_prime:
            primes.append(num)

    return primes


def get_valid_input(prompt):
    """Get a valid numeric input from the user."""

    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                raise ValueError("The number must be non-negative.")

            return value

        except ValueError as e:
            print(e)


# from prime_generator import generate_primes, get_valid_input


class TestPrimeGenerator(unittest.TestCase):
    """Tests for the prime number generator and input validation functions."""

    def test_generate_primes_valid(self):
        """Test valid prime number generation."""
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])
        self.assertEqual(generate_primes(2), [2])
        self.assertEqual(generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_generate_primes_invalid_limit(self):
        """Test invalid limit for prime generation."""
        with self.assertRaises(AssertionError):
            generate_primes(1)  # Below valid range
        with self.assertRaises(AssertionError):
            generate_primes("ten")  # Non-numeric input
        with self.assertRaises(AssertionError):
            generate_primes(-5)  # Negative number

    def test_get_valid_input(self):
        """Test get_valid_input with valid and invalid inputs."""
        # Since `input()` is used, this requires user simulation or mocking.
        # Mocking would replace `input()` with predefined values for testing.
        import builtins

        original_input = builtins.input

        # Test valid input
        builtins.input = lambda _: "10"
        self.assertEqual(get_valid_input("Enter a number: "), 10.0)

        # Test invalid inputs (mocking a sequence of attempts)
        attempts = iter(["-5", "abc", "2.5"])
        builtins.input = lambda _: next(attempts)
        self.assertEqual(get_valid_input("Enter a number: "), 2.5)

        # Restore original input
        builtins.input = original_input


if __name__ == "__main__":
    unittest.main()
