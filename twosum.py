class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        list = [0,0]
    
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target:
                    if i != j:
                       list = [i,j]
                

        return list 
    

nums = [2,7,11,15]
target = 9 
print(Solution.twoSum(Solution, nums, target))