class Solution:
    def sortString(self, s: str) -> str:
        s=list(s)
        s.sort()
        r=[]
        while True:
            if len(s)==0:
                break
            t=list(set(s))
           
            t.sort()
           
            for i in t:
                r.append(i)
                s.remove(i)
           
            t=list(set(s))
            t.sort()
          
            for i in range(len(t)-1,-1,-1):
               
                r.append(t[i])
                s.remove(t[i])
                
        return "".join(r)