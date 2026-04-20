class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque(nums[:k])
        cur_max = max(q)  
        res.append(cur_max)
        
        for r in range(k, len(nums)):
            removed = nums[r - k]
            added = nums[r]
            q.popleft()
            q.append(added)
            
            if added >= cur_max:
                cur_max = added          
            elif removed == cur_max:
                cur_max = max(q)         
            
            res.append(cur_max)
        
        return res