class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Anagrams should have same length
        # 2. Also, have same exact characters
        # 3. Therefore, sorting in this case guarante both conditions
        return sorted(s) == sorted(t)
        