class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temperature in enumerate(temperatures): 
            while stack and temperature > stack[-1][1]:
                old_index = stack[-1][0]
                stack.pop()
                result[old_index] = i - old_index
            stack.append((i, temperature))
        return result

            

        