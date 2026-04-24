class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. I already have an answer in the hashmap
        anagrams = {}
        # 2. Check if the string exist in the hashmap
        for s in strs:
            key = ''.join(sorted(s))

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(s)
        return list(anagrams.values())
                
        # 3. If exist, add it, otherwise remove it 