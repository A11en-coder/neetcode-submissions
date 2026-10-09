class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize the hashmap
        hashmap = {}
    
        for index, num in enumerate(nums):
        
            # set the require
            require = target - num

            # if the require is in the hashmap, then return the pair
            if require in hashmap:
                return [hashmap[require], index]
            
            # move on to the next num
            hashmap[num] = index
