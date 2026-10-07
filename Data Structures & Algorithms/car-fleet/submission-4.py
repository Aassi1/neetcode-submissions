class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for p, s in cars:
            time = (target -  p) / s
            if not stack : 
                stack.append(time)
            else:
                if time <= stack[-1] :
                    pass
                else:
                    stack.append(time)

        return len(stack)

        
        