class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        while l <= r:
            hours = 0
            m = (l + r) // 2

            for pile in piles:
                hours += math.ceil(pile/m)

            if hours > h :
                l = m + 1
            elif hours <= h:
                r = m - 1

        return l

        