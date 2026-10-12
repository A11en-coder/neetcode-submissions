class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        
        for i, a in enumerate(nums):
            # set the first value 
            if a == nums[i - 1] and i > 0:
                continue

            # use two-pointer to find 2 sum
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[l] + nums[r] + a
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], a])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
