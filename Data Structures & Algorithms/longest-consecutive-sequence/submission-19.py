class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set()
        maxLength = 0
        currentLength = 0

        for num in nums:
            seen.add(num)

        for num in nums:
            if num-1 not in seen :
                currentLength = 1
                while num + 1 in seen :
                    currentLength += 1
                    num += 1

                maxLength = max(maxLength,currentLength)


        length = int(max(currentLength, maxLength))

        return length
        