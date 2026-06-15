class Solution(object):
    def twoSum(self, nums, target):
        d = {}

        for i, num in enumerate(nums):
            x = target - num

            if x in d:
                return [d[x], i]

            d[num] = i