'''
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
'''



#Here is the solution 1 which is done by comparing two strings 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
           
        ptr1=0 
        ptr2=0
        
        while ptr1<len(s)-1 or ptr2<=len(t)-1:
            
            if(ptr1>len(s)-1 or ptr2> len(t)-1):
                break
            if(s[ptr1]==t[ptr2]):
                ptr1+=1
                ptr2+=1
            else:
                ptr2+=1
        
        if (ptr1==len(s)):
            return True
        
        return False
      
# Here is the solution 2 which uses deque for comparison

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        
        queue=collections.deque(s)
        
        for i in t:
            if not queue:
                return True
            if(queue[0]==i):
                queue.popleft()
        return not queue        
