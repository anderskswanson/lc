class Solution():
    def __init__(self):
        self._result = []

    def permute(self, nums):
        return [i for i in self.helper(nums)]

    def helper(self, nums):
        if len(nums) < 2:
            yield nums
        else:
            for i in self.helper(nums[1:]):
                for j in range(len(nums)):
                    yield i[:j] + nums[0:1] + i[j:]

