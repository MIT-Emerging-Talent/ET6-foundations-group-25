import unittest
from solutions.names_sorter import get_first_name, display_sorted_names


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
            get_first_name(("Smith",))  # Invalid: Tuple with fewer than 2 elements
        with self.assertRaises(ValueError):
            get_first_name(
                ("Smith", "John", "Extra")
            )  # Invalid: Tuple with more than 2 elements

    def test_display_sorted_names_valid(self):
        """Test display_sorted_names with valid input data."""
        # Should display names sorted by first name
        names_dict = {"Yusif": "Arwa", "Smith": "John"}
        import io
        from contextlib import redirect_stdout

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "1. Arwa Yusif\n2. John Smith\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_sorted_names_tie(self):
        """Test display_sorted_names when duplicate first names are present."""
        # Should sort by last name when first names are identical
        names_dict = {"Smith": "John", "Johnson": "John"}
        import io
        from contextlib import redirect_stdout

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "1. John Johnson\n2. John Smith\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_sorted_names_empty(self):
        """Test display_sorted_names with an empty dictionary."""
        # Should handle empty input gracefully
        names_dict = {}
        import io
        from contextlib import redirect_stdout

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "No names to display.\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_sorted_names_invalid(self):
        """Test display_sorted_names with invalid inputs."""
        # Should raise TypeError for non-dictionary inputs
        with self.assertRaises(TypeError):
            display_sorted_names(["Smith", "John"])  # Invalid: Not a dictionary
        with self.assertRaises(TypeError):
            display_sorted_names({"Smith": 123})  # Invalid: Non-string value
        with self.assertRaises(TypeError):
            display_sorted_names({123: "John"})  # Invalid: Non-string key


if __name__ == "__main__":
    unittest.main()
