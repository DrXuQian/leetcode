class Solution:
    def isPalindrome(self, s: str) -> bool:
        int_s = []
        for c in s:
            if 0 <= ord(c) - ord('a') < 26:
                int_s.append(ord(c))
            elif 0 <= ord(c) - ord('A') < 26:
                int_s.append(ord(c) - ord('A') + ord('a'))
            elif 0 <= ord(c) - ord('0') <= 9:
                int_s.append(ord(c))
        return int_s == int_s[::-1]

print(Solution().isPalindrome(" apG0i4maAs::sA0m4i0Gp0"))