class Solution:
    def maximum69Number (self, num: int) -> int:
        list=[]
        for i in str(num):
            list.append(i)
        if '6' in list:
            list[list.index('6')]='9' 
        else:
            list=list
        list=''.join(list)
        return list
        
        
        