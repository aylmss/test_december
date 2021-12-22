class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        counter=0   
        for i in range(len(words)): 
            for j in words[i]:
                if j not in allowed:
                    counter+=1
                    break
        return len(words)-counter
        
        
#         allowed0=[]
#         counter=0
#         for i in allowed:
#               allowed0.append(i)
#         for i in range(len(words)): 
#             for j in allowed:
#                 diff=list((set(words[i])).difference(set(allowed0)))
#                 if diff!=[]:
#                     continue
#                 else:
#                     counter+=1
#         return int(counter/2)
