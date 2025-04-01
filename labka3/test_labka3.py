import unittest
from labka3 import (
    remove_special_chars,
    match_word_with_char,
    match_word_with_length,
    match_specific_words,
    extract_money,
    clean_python_code,
    convert_date_format,
)

class TestExercise4(unittest.TestCase):
    def test_remove_special_chars(self):
        self.assertEqual(remove_special_chars("hello@world!"), "helloworld")
        self.assertEqual(remove_special_chars("123#456"), "123456")
        self.assertEqual(remove_special_chars("no_special_chars"), "no_special_chars")
        self.assertEqual(remove_special_chars(""), "")

    def test_match_word_with_char(self):
        self.assertEqual(match_word_with_char("apple banana cherry", "a"), ["apple", "banana"])
        self.assertEqual(match_word_with_char("cat caterpillar cactus", "c"), ["cat", "caterpillar", "cactus"])
        self.assertEqual(match_word_with_char("dog elephant frog", "z"), [])
        self.assertEqual(match_word_with_char("Apple Banana Cherry", "A"), ["Apple"])
        self.assertEqual(match_word_with_char("hello-world hello_world", "-"), ["hello-world"])

    def test_match_word_with_length(self):
        self.assertEqual(match_word_with_length("apple banana cherry", 5), ["apple"])
        self.assertEqual(match_word_with_length("cat dog elephant", 3), ["cat", "dog"])
        self.assertEqual(match_word_with_length("one two three", 4), [])
        self.assertEqual(match_word_with_length("short long", 10), [])

    def test_match_specific_words(self):
        self.assertEqual(match_specific_words("apple bananas apricots"), ["bananas", "apricots"])
        self.assertEqual(match_specific_words("Apples and Berries"), ["Apples", "Berries"])
        self.assertEqual(match_specific_words("no matches here"), [])
        self.assertEqual(match_specific_words("aBs abs"), ["aBs", "abs"])

    def test_extract_money(self):
        self.assertEqual(extract_money("$10 $20.5 $30"), ([10.0, 20.5, 30.0], 60.5))
        self.assertEqual(extract_money("no money here"), ([], 0))
        self.assertEqual(extract_money("$100"), ([100.0], 100.0))
        self.assertEqual(extract_money("$5.5 $4.5"), ([5.5, 4.5], 10.0))

    def test_clean_python_code(self):
        code = "x = 1  # This is a comment\n\n\ny = 2\n\n"
        cleaned_code = "x = 1\ny = 2"
        self.assertEqual(clean_python_code(code), cleaned_code)
        self.assertEqual(clean_python_code("# Only comments\n\n"), "")
        self.assertEqual(clean_python_code(""), "")

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("2023-10-05"), "05-10-2023")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")
        self.assertEqual(convert_date_format("no date here"), "no date here")
        self.assertEqual(convert_date_format("2023-01-01 and 2024-02-02"), "01-01-2023 and 02-02-2024")

if __name__ == "__main__":
    unittest.main()