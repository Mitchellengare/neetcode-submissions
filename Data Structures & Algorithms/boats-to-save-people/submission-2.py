class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l, r = 0, n-1
        count = 0

        while l <= r:
            target = people[l] + people[r]
            if target <= limit:
                count+=1
                l+=1
                r-=1
            else:
                r-=1
                count+=1
        
        return count
            
