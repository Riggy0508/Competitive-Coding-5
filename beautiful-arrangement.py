# TC: O(N) #Number of permutations
# SC: O(Depth of the tree)

class Solution:
    def countArrangement(self, n: int) -> int:
        self.count=0
        
        nums=[i for i in range(1,n+1)]
        
        
        
        def dfs(nums,i:int=1):
            if i==n+1:
                self.count+=1
                return
            
            
            for j,val in enumerate(nums):
                if not(val%i and i%val):
                    dfs(nums[:j]+nums[j+1:],i+1)
        
        dfs(nums)
        return self.count