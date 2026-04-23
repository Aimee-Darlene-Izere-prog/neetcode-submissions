class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Create an array to keep track of seen values that does not satify the requirements
        seen_values = {}
        counter = 0
        
        # 2. compare one value to other values before it
        for i in range(len(nums)):
            for j in range(len(seen_values)):
                if nums[i] + seen_values[j] == target and i != j:
                    return [j,i]
            seen_values[counter] = nums[counter]
            counter += 1
            
        #  if nums[i] + get.
        # 3. continue