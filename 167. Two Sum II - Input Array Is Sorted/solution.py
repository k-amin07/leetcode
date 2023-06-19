from typing import List
class Solution:
    def binarySearch(self,A,n,left,right):
        if(right<=left):
            return -1
        mid = (left + right) // 2
        if(A[mid] == n):
            return mid
        elif(A[mid] > n):
            return self.binarySearch(A,n,left,mid)
        else:
            return self.binarySearch(A,n,mid+1,right)
    
    ## this approach uses binary search, takes O(nlog(n)) time
    def twoSum_initial(self, numbers: List[int], target: int) -> List[int]:
        for index,value in enumerate(numbers):
            temp = target - value
            if temp < value:
                continue
            otherIndex = self.binarySearch(numbers,temp,index,len(numbers))
            if(otherIndex != -1):
                return [index+1,otherIndex+1]
    # this approach is similar to the regular two sum approach. Takes O(n) time.        
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for index,value in enumerate(numbers):
            if value in dic:
                return dic[value]+1,index +1
            else:
                dic[target-value] = index

