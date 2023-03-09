from unittest import TestCase
from exceptions_quiz import reverse_concat


class TestReverseConcat(TestCase):
    def test_reverse_concat_standard(self):
        self.assertEqual("This Is Reversed", reverse_concat("desreveR", " sI sihT"))
