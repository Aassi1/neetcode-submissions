class Solution:
    def trap(self, height: List[int]) -> int:
        # Input: height = [0,2,0,3,1,0,1,3,2,1]
        # Output should be 9
        # Lets try to find the formula here, knowing its a 2 pointer problem 
        # what im thinknig is this : is the wall to my left smaller than the wall to my right, if so, no water can be stored and we move on, else water can be stored 
        # i know we will have to use min somewhere as we will have to take the minimum of the 2 walls
        # The water formula would be min(tallest wall seen on left, tallest wall see on right) - current height
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                water += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += rightMax - height[r]

        return water