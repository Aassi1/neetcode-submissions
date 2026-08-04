class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen  = set()

        for num in nums:
            seen.add(num)
            print("added to set")
                                        
                
        return not (len(seen) == len(nums))
