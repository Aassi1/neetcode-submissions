class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = {}
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
            print(count)

        buckets = [[] for _ in range (len(nums)+1)]

        for num, freq  in count.items():
            buckets[freq].append(num)
            print(buckets)

        for i in range( len(buckets) -1 , -1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


        


