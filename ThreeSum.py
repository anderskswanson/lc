class Solution():
    def threeSum(self, nums):
        triplets = []

        if len(nums) < 3:
            return triplets
        nums = sorted(nums)

        end = len(nums)
        for i in range(end-2):
            # start with smallest and largest
            j = i + 1
            k = end - 1
            val = -nums[i]
            while j < k:
                if nums[j] + nums[k] < val:
                    j += 1
                elif nums[j] + nums[k] > val:
                    k -= 1
                else:
                    # we have a triple here
                    triple = [nums[i], nums[j], nums[k]]
                    triple.append(triple)
                    # since we are sorted, move to next
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

            while i < end - 2 and nums[i] == nums[i+1]:
                i += 1
        return triplets

