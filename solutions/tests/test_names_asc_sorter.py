"""Unit tests for the name sorting module.

This module contains unit tests for the functions `display_sorted_names` and
`get_first_name` in the `solutions.names_asc_sorter` module. It tests various
scenarios, including valid and invalid inputs, empty input, ties in first
names,
and mixed-case names.
"""

import io
import unittest
from contextlib import redirect_stdout

from solutions.names_asc_sorter import (
    display_sorted_names,
    get_first_name,
)


class TestNameSorting(unittest.TestCase):
    """Unit tests for the name sorting module."""

    def test_get_first_name_valid(self):
        """Test get_first_name with valid inputs."""
        # Should return the first name when given a valid tuple
        self.assertEqual(get_first_name(("Yusif", "Arwa")), "Arwa")
        self.assertEqual(get_first_name(("Smith", "John")), "John")

    def test_get_first_name_invalid(self):
        """Test get_first_name with invalid inputs."""
        # Should raise TypeError when input is not a tuple
        with self.assertRaises(TypeError):
            get_first_name(["Smith", "John"])  # Invalid: Not a tuple

        # Should raise ValueError when tuple does not have exactly two elements
        with self.assertRaises(ValueError):
            get_first_name(("Smith",))
        # Invalid: Tuple with fewer than 2 elements
        with self.assertRaises(ValueError):
            get_first_name(
                ("Smith", "John", "Extra")
            )  # Invalid: Tuple with more than 2 elements

    def test_display_sorted_names_valid(self):
        """Test display_sorted_names with valid input data."""
        # Should display names sorted by first name
        names_dict = {"Yusif": "Arwa", "Smith": "John"}

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "1. Arwa Yusif\n2. John Smith\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_sorted_names_tie(self):
        """
        Test display_sorted_names when duplicate first names are present.
        """
        # Should sort by last name when first names are identical
        names_dict = {"Smith": "John", "Johnson": "John"}

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "1. John Johnson\n2. John Smith\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_sorted_names_empty(self):
        """Test display_sorted_names with an empty dictionary."""
        # Should handle empty input gracefully
        names_dict = {}

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "No names to display.\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_sorted_names_invalid(self):
        """Test display_sorted_names with invalid inputs."""
        # Should raise TypeError for non-dictionary inputs
        with self.assertRaises(TypeError):
            display_sorted_names(["Smith", "John"])
        # Invalid: Not a dictionary
        with self.assertRaises(TypeError):
            display_sorted_names({"Smith": 123})  # Invalid: Non-string value
        with self.assertRaises(TypeError):
            display_sorted_names({123: "John"})  # Invalid: Non-string key

    def test_display_sorted_names_mixed_case(self):
        """Test display_sorted_names with mixed case names."""
        # Should sort names in a case-insensitive manner
        names_dict = {"smith": "john", "Johnson": "john"}

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "1. john Johnson\n2. john smith\n"
        self.assertEqual(output.getvalue().lower(), expected_output.lower())


if __name__ == "__main__":
    unittest.main()
