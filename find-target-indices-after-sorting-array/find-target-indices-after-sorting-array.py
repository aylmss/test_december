class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counter1=0
        counter2=0
        for i in range(len(nums)):
            if nums[i]==target:
                counter1+=1
            if nums[i]<target:
                counter2+=1
        if counter1==0:
                return []
        list=[counter2]
        while counter1>1:
            counter2+=1
            list.append(counter2)
            counter1-=1
        return list
    