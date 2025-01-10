import unittest
from names_sorter import get_first_name, display_sorted_names


class TestNameSorting(unittest.TestCase):
    """Unit tests for name sorting module."""

    def test_get_first_name_valid(self):
        """Test get_first_name with valid inputs."""
        self.assertEqual(get_first_name(("Yusif", "Arwa")), "Arwa")
        self.assertEqual(get_first_name(("Smith", "John")), "John")

    def test_get_first_name_invalid(self):
        """Test get_first_name with invalid inputs."""
        with self.assertRaises(TypeError):
            get_first_name(["Smith", "John"])  # Not a tuple
        with self.assertRaises(ValueError):
            get_first_name(("Smith",))  # Tuple with fewer than 2 elements
        with self.assertRaises(ValueError):
            get_first_name(
                ("Smith", "John", "Extra")
            )  # Tuple with more than 2 elements

    def test_display_sorted_names_valid(self):
        """Test display_sorted_names with valid data."""
        names_dict = {"Yusif": "Arwa", "Smith": "John"}
        import io
        from contextlib import redirect_stdout

        output = io.StringIO()
        with redirect_stdout(output):
            display_sorted_names(names_dict)

        expected_output = "1. Arwa Yusif\n2. John Smith\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_sorted_names_tie(self):
        """Test display_sorted_names with duplicate first names."""
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
        with self.assertRaises(TypeError):
            display_sorted_names(["Smith", "John"])  # Not a dictionary
        with self.assertRaises(TypeError):
            display_sorted_names({"Smith": 123})  # Non-string value
        with self.assertRaises(TypeError):
            display_sorted_names({123: "John"})  # Non-string key


if __name__ == "__main__":
    unittest.main()
