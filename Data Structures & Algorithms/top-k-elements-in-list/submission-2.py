class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for v in nums:
            if v in dic:
                dic[v] = dic[v]+1
            else:
                dic[v] = 1
            
        return sorted(dic, key=dic.get, reverse=True)[:k]
        
        
