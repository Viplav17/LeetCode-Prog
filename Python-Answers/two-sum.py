class Solution:
    def twoSum(self, nums, target: int):
        temp_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in temp_nums:
                return ([temp_nums[target - nums[i]], i])
            else:
                temp_nums[nums[i]] = i


