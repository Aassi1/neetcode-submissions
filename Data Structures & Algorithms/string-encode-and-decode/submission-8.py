class Solution:

    def encode(self, strs: List[str]) -> str:

        result = []

        for s in strs:
            length = str(len(s))

            newS = length + "#" + s

            result.append(newS)
        
        result = "".join(result)

        return result


    def decode(self, s: str) -> List[str]:
        result = []
        
        i = 0

        while i < len(s):
            position  = s.find("#", i)
            length = int(s[i:position])

            startOfNewS = position + 1

            newS = s[startOfNewS:startOfNewS + length]

            result.append(newS)

            i = startOfNewS + length

        return result
        
