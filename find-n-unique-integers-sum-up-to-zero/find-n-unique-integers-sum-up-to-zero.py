class Solution:
    def sumZero(self, n: int) -> List[int]:
        list = []
    
        for i in range(n // 2):
            list.append(i + 1)
            list.append((-1) * (i + 1))
        
        if n % 2 == 1:
            list.append(0)
        
        return list