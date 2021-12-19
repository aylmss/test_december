class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter=0
        while num!=0:
            if num%2==0:
                num/=2
                counter+=1
            elif num%2==1:
                num-=1
                counter+=1
            else:
                counter+=1
                continue 
                
        return counter
            
            
                