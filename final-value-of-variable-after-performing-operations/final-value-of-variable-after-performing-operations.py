class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for i in range(len(operations)):
            if operations[i]=='--X' or operations[i]=='X--':
                ans-=1
            if operations[i]=='++X' or operations[i]=='X++':
                ans+=1
        return ans