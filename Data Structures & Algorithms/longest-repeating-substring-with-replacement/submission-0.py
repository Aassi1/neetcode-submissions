class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, best, max_freq = 0, 0, 0 
        frequencies = {}

        for right in range(len(s)) : 
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1
            max_freq = max(max_freq, frequencies[s[right]])

            while (right - left + 1) - max_freq > k:
                frequencies[s[left]] -= 1
                left +=1

            best = max(best, right - left + 1)
        return best
        