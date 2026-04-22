class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res = defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1

            key = tuple(cnt)
            res[key].append(s)
        
        return list(res.values())
   