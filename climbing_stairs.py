#takes n steps to reach the top 
#each time 1 or 2 steps 
# in how many distinct ways can you climb to the top? 

class Solution: 
   
    def climbStairs(self, n:int) -> int:
        #dynamic programming with memorization 
        # the last flight of stairs can either be taken in 1 or 2 
        if n not in self.dic:
           self.dic[n] = self.climbStairs(n-1)+ self.climbStairs(n-2)
        
        return self.dic[n]
    
print(Solution.climbStairs(3))

