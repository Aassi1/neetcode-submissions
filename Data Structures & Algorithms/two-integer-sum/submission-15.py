class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Here we have to create a hashmap 
        prevMap = {} # here the value will be the 

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap :
                return [prevMap[diff], i]

            prevMap[n] = i

            