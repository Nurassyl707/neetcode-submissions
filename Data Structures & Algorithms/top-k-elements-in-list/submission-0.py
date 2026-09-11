class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        sorted_freq = sorted(freq, key=lambda x: freq[x], reverse=True)

        return sorted_freq[:k]
