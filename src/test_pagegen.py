import unittest
from pagegen import *


class TestPagegen(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
Test
## Heading 2
# Heading 1
"""
        title = extract_title(markdown)
        self.assertEqual(title, "Heading 1")

    def test_extract_title_error(self):
        markdown = """
Test
### Heading 3

Orange
"""
        self.assertRaises(Exception, extract_title, markdown)


if __name__ == "__main__":
    unittest.main()
