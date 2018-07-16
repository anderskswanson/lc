class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dupes = 0
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                dupes += 1
            else:
                nums[i - dupes] = nums[i]
        return n - dupes
