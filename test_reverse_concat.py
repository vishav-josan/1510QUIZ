from unittest import TestCase
from exceptions_quiz import reverse_concat


class TestReverseConcat(TestCase):
    def test_reverse_concat_standard(self):
        self.assertEqual("This Is Reversed", reverse_concat("desreveR", " sI sihT"))

    def test_reverse_concat_value_error_first_word(self):
        with self.assertRaises(ValueError):
            reverse_concat("", " sI sihT")

    def test_reverse_concat_value_error_second_word(self):
        with self.assertRaises(ValueError):
            reverse_concat("placeholder", "")

    def test_reverse_concat_type_error_first_word(self):
        with self.assertRaises(TypeError):
            reverse_concat(1, "hello")

    def test_reverse_concat_type_error_second_word(self):
        with self.assertRaises(TypeError):
            reverse_concat("something new", True)

    def test_reverse_concat_type_error_second_word_raises_value_error(self):
        with self.assertRaises(TypeError):
            reverse_concat(False, "")
