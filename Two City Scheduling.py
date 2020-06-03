'''
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 
.
Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000

'''



#Approch 1 with the time complexity of O(N)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1]-x[0])
        total_cost=0
        print(costs)
        i=0
        while i < (len(costs)//2):
            total_cost+=costs[i][1]
            i+=1
        while i < (len(costs)):
            total_cost+=costs[i][0]
            i+=1
        return total_cost    
        
#Approch 2 with the the time complexity of O(N) but bit faster

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1]-x[0])
        total_cost=0
        half_length=(len(costs)//2)
        
        
        
        for i in range(half_length):
            total_cost += costs[i][1] + costs[i+half_length][0]
            
        return total_cost    
            
