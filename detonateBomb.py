class Solution:
    


    def findDetonation(self, bombs:list[list[int]], bomb:list[int]) -> int:
        x = bomb[0]
        y = bomb[1]
        r = bomb[2]
        count = 0
        #print("x = ", x, "y = ", y, "r =", r)

        for b in bombs:
            print(b)
            l = (b[0]-x)**2 + (b[1]-y)**2
            if l <= (r**2):
                count+=1
        
        return count
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        
        max = 0
        for b in bombs:
            num = Solution.findDetonation(Solution,bombs,b)
            print(num)
            if (num > max):
                max = num        
        return max

#bombs = [[1,1,100000],[100000,100000,1]]
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]

print(Solution.maximumDetonation(Solution, bombs))