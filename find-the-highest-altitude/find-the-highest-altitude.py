class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=[0]
        sum=0
        for i in range(len(gain)):
            sum+=gain[i]
            alt.append(sum)
        return max(alt)
     