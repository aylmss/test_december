class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
        
        
        
        
        # backwards=words
        # bw1=[]
        # counter=0
        # for i in backwards:
        #     bw1.append(i[ : :-1])
        # diff= list(set(words).intersection(set(bw1)))
        # for i in range(len(words)):
        #     for word in diff:
        #         if words[i]==word:
        #             return words[i]
        #             counter+=1  
        #         else:
        #             continue
        # if counter==0:
        #     return ""
      
                    
                
  