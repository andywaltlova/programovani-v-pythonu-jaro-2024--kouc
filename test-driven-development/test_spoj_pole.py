import unittest

from funkce import spoj_pole_do_vety


class TestSpojPole(unittest.TestCase):
    def test_no_trailing_whitespaces(self):
        # assert spoj_pole_do_vety(["a", "b", "c"]) == "a b c"
        self.assertEqual(spoj_pole_do_vety(["a", "b", "c"]), "a b c")

        assert spoj_pole_do_vety(["a"]) == "a"
        assert spoj_pole_do_vety([]) == ""

        self.assertRaises(TypeError, spoj_pole_do_vety, 0)



