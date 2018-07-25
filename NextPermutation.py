class Solution():
    def nextPermutation(self, nums):
        flag = True
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                flag = False
                break
        if flag:
            return nums[::-1]

        
        return nums


