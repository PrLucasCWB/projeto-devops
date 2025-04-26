from django.test import TestCase

class SimpleTest(TestCase):
    def test_soma(self):
        self.assertEqual(1 + 1, 2)

class ExampleTestCase(TestCase):
    def test_soma(self):
        self.assertEqual(1 + 1, 2)

    def test_subtracao(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplicacao(self):
        self.assertEqual(3 * 4, 12)

    def test_divisao(self):
        self.assertEqual(10 / 2, 5)

    def test_string(self):
        self.assertEqual("devops".upper(), "DEVOPS")

