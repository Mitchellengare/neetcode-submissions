class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for v in nums:
            dic[v] = dic.get(v, 0) + 1
            
        return sorted(dic, key=dic.get, reverse=True)[:k]
        
        
