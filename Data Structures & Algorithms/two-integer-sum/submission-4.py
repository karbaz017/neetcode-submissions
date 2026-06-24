class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for ind, num in enumerate(nums):
            value = target - num

            if value in seen:
                return [seen[value], ind]
            else:
                seen[num] = ind
