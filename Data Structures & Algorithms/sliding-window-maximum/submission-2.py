class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque(nums[:k])
        cur_max = max(q)  # only once upfront
        res.append(cur_max)
        
        for r in range(k, len(nums)):
            removed = nums[r - k]
            added = nums[r]
            q.popleft()
            q.append(added)
            
            if added >= cur_max:
                cur_max = added          # new element beats current max
            elif removed == cur_max:
                cur_max = max(q)         # lost the max, must rescan
            
            res.append(cur_max)
        
        return res