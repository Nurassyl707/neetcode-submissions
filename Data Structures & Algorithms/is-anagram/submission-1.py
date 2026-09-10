class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = set(s)
        if len(s) != len(t):
            return False
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        return True