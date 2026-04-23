class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Create a hashmap 
        seen_values = {}
        # counter = 0

        # 2. compare one value to other values before it
        for i in range(len(nums)):
            # what number I am looking for? Is there anyway of looking for it? 
            target_num = target - nums[i]
            if seen_values.get(target_num) != None:
                return [seen_values[target_num], i]
            
            seen_values[nums[i]] = i

            #  if nums[i] + get
            # 3. continue