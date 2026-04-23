class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       return len(nums) != len(set(nums))

        #### MY SOLUTION ###
        # Hash Mapping
        # I don't know how to create a hashmap in here? 
        # Is there an existing algorithm built in here for hashmap? 

        # Key: value in the array
        # value: number of times the value in present in the array

        # lwk, I can just create another array, but hashmap would 
        # allow me to to use the get method

        # 1. create a hash map
        # hash = dict.fromkeys(range(len(nums), 0))
        # hash = {}
        # 2. loop through the given array
        #for n in nums:
            #if hash.get(n) == 1:
                #return True
            # n does not exist, put it in the has after checking
            #hash[n] = 1 # One means seen 
             
        # return False 
        # 3. if an element in the array exist in hashmap, return directly false
        # 4. Else, after looping, return true
        