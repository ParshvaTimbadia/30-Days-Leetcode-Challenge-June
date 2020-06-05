'''
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

'''




class Solution:

    def __init__(self, w: List[int]):
        self.sum_list=[]
        self.sum=0
        temp_sum=0
        
        for i in w:
            temp_sum+=i
            self.sum_list.append(temp_sum)
        self.sum=temp_sum    
        

    def pickIndex(self) -> int:
        
        random_num = self.sum*random.random()
        low, high = 0, len(self.sum_list)
        while low< high:
            mid = low+(high-low)//2
            if random_num > self.sum_list[mid]:
                low=mid+1
            else:
                high=mid
        return low    
        
