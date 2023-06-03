class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        children = [[]for i in range(n)] #children array for all n employees 
        for i,m in enumerate(manager): #i is the index, m is the content 
            if m >=0: children[m].append(i) #adding to children array if manager[i] is not -1 
        
        def dfs(i):
            max = 0
            for j in children[i]:
                if (dfs(j)>max):
                    max = dfs(j)
            return max + informTime[i]
        #return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        

        return dfs(headID)


n= 6
headID = 2
informTime =[0,0,1,0,0,0]
manager =[2,2,-1,2,2,2]

print(Solution.numOfMinutes(Solution,n,headID,manager,informTime))

