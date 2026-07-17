class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i,word in enumerate(strs):
            sorted_str = "".join(sorted(word))
            if sorted_str not in seen:
                seen[sorted_str] = [word]
            else:
                seen[sorted_str].append(word)
        return list(seen.values())