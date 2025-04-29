import unittest

from utils_project.utils import group_anagrams, sum_of_primes, to_title_case


class TestUtilityFunctions(unittest.TestCase):

    def setUp(self):
        self.test_cases_sum_of_primes = [
            (10, 17),
            (1, 0),
            (2, 2),
            (13, 41),
            (15, 41)
        ]

        self.test_cases_convert_to_title_case = [
            ("hello world", "Hello World"),
            ("python programming", "Python Programming"),
            ("AnoTher teSt CasE", "Another Test Case"),
            ("", ""),
            ("a b c d", "A B C D"),
            (" extra  spaces   here", " Extra  Spaces   Here"),
            ("test@home", "Test@Home"),
            ("hello-world", "Hello-World"),
            ("python_101 !special", "Python_101 !Special"),
        ]

        self.test_cases_group_anagrams = [
            (["eat", "tea", "tan", "ate", "nat", "bat"], {frozenset(["eat", "tea", "ate"]),
                                                          frozenset(["tan", "nat"]),
                                                          frozenset(["bat"])}),
            (["", "", ""], {frozenset(["", "", ""])}),
            (["abc", "cab", "bca", "def", "fed"], {frozenset(["abc", "cab", "bca"]), frozenset(["def", "fed"])}),
            (["a", "a", "a", "a", "a"], {frozenset(["a", "a", "a", "a", "a"])}),
            (["", "eat", "abc", "a"], {frozenset(["eat"]), frozenset(["abc"]), frozenset(["a"]), frozenset([""])})
        ]

    def test_sumOfPrimes_ValidInputs_CorrectSumReturned(self):
        for n, expected_sum in self.test_cases_sum_of_primes:
            with self.subTest(n=n):
                self.assertEqual(sum_of_primes(n), expected_sum)

    @unittest.skip("skip")
    def test_convertToTitleCase_ValidInputs_CorrectTitleCaseReturned(self):
        for input_text, expected_text in self.test_cases_convert_to_title_case:
            with self.subTest(input_text=input_text):
                self.assertEqual(to_title_case(input_text), expected_text)

    def test_groupAnagrams_ValidInputs_CorrectGroupsReturned(self):
        for input_list, expected_set in self.test_cases_group_anagrams:
            with self.subTest(input_list=input_list):
                output = set(frozenset(group) for group in group_anagrams(input_list))
                self.assertEqual(output, expected_set)

    def test_test(self):
        self.assertEqual(0.0000000000000015 *3, 0.0000000000000045)


if __name__ == '__main__':
    unittest.main()
