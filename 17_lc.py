from typing import List


class Solution:
    def addLetterToCombination(self, combination: List[str], letter, lut):
        digits = lut[letter]
        new_combination = []
        for c in combination:
            for d in digits:
                new_combination.append("".join([c, d]))
        return new_combination


    def letterCombinations(self, digits: str) -> List[str]:
        lut = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']
               }
        if not digits:
            return []
        combinations = ['']
        for d in digits:
            combinations = self.addLetterToCombination(combinations, d, lut)
        return combinations

Solution().letterCombinations("")