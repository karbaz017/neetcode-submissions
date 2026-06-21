class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = {}

        for i in range(len(nums)):
            if nums[i] in new_nums:
                return True
            else:
                new_nums[nums[i]] = 1

        return False