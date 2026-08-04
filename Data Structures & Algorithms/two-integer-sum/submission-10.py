class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in Hmap:
                return [Hmap[diff], i]
            Hmap[n] = i 
            