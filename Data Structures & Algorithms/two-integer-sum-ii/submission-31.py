class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while numbers[left_index] <= numbers[right_index]:
            if target > numbers[left_index] + numbers[right_index]:
                left_index += 1
            elif target < numbers[left_index] + numbers[right_index]:
                right_index -= 1 
            else: 
                return [left_index + 1, right_index + 1]
                
        return [left_index + 1, right_index + 1]

            
            
        