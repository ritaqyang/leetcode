class Solution:
    


    def findDetonation(self, bombs:list[list[int]], bomb:list[int]) -> int:
        x = bomb[0]
        y = bomb[1]
        r = bomb[2]
        count = 0
        #print("x = ", x, "y = ", y, "r =", r)

        for b in bombs:
            print(b)
            if b[0]>=(x-r) & b[0]<=(x+r):
                print("x is right")
                if b[1]>=(y-r)& b[1]<=(y+r):
                    print("y is within range")
                    count +=1
        
        
        return count
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        
        max = 0
        for b in bombs:
            num = Solution.findDetonation(Solution,bombs,b)
            if (num > max):
                max = num        
        return max

bombs = [[1,1,5],[10,10,5]]

print(Solution.maximumDetonation(Solution, bombs))