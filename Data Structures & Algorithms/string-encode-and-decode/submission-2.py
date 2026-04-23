class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        O(N2)
        """
        res = ""
        for s in strs:
            res += f"{str(len(s))}#{s}"
        return res


    def decode(self, s: str) -> List[str]:
        """
        O(N)
        """
        res = []

        i = 0
        while i < len(s):
            num_str = ""
            word_str = ""

            while s[i] != "#":
                num_str += s[i]
                i += 1

            num = int(num_str)
            i += 1

            word_str += s[i:i+num]
            res.append(word_str)
            i += num
            
        return res



