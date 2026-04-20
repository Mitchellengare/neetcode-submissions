class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
     

        res =[]
        combs = []
        nums = list(range(1, n+1))

        def dfs(start):
            if len(combs) == k :
                res.append(combs.copy())
                return
                
            for i in range(start, len(nums)):
                combs.append(nums[i])
                dfs(i+1)
                combs.pop()
               

        dfs(0)
        return res



                



            
        