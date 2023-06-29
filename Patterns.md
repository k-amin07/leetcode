Listing down the general idea and my understanding of the programming patterns mentioned in [this repo](https://github.com/dipjul/Grokking-the-Coding-Interview-Patterns-for-Coding-Questions).

# Table of Contents
1. [Sliding Window (Constant Size)](#sliding-window-constant-size)
2. [Sliding Window (Dynamic Size)](#sliding-window-dynamic-size)
3. [When to Use Sliding Window](#when-to-use-sliding-window)

## Sliding Window (Constant Size)

[This video](https://www.youtube.com/watch?v=GcW4mgmgSbw) sums it up nicely. Imagine we have an array and we want to find the sum of all subarrays of size 3. For instance let the array be nums = \[1,2,3,4,5\]. 

**Naive Solution** 
- It is easy to calculate `nums[1] + nums[2] + nums[3]` and then `nums[2] + nums[3] + nums[4]` and so on. 
- However, we are recomputing a lot of sums. In the above example, we are computing `nums[2]+nums[3]` twice and we'll end up with an time complexity of $O(N*k)$.
- In terms of loops, this is equivalent to an outer loop running $N$ times for an array of size $N$, and an inner loop running $k$ times for each set of k elements in the array.

**Better Solution**
- The better way of doing this is to calculate `sum1 = nums[1] + nums[2] + nums[3]` for the first set of $k=3$ numbers and then calculating and then for the next three numbers, we calculate `sum1 - nums[1] + nums[4]` and so on.
- With this approach we reduce the number of iterations down to a single loop that runs $N$ times, making the time complexity $O(N)$. We only calculate sum of k elements once and then add and subtract one element in each iteration. The impact is even more evident when $K$ is larger as the number of iterations of the inner loop in naive approach will increase.

## Sliding Window (Dynamic Size)
The video linked above also explains the dynamic sliding window pattern. In many cases, we need to find the largest or smallest window that satisfies a certain criteria. For instance, given an array [1,2,3,4,5,6] and we need to find the minimum length sub array who's sum is at least 7 (can be greater as well). We can sum up the whole thing, but we need the smallest subarray. We dont know what size our subarray needs to be. The approach goes as follows
- Start from size 1 and keep expanding the subarray until we get a sum greater than the required sum (7 in our example).
- Start decreasing the subarray from the left until we get the minimum size subarray that is greater than or equal to the required sum.
- Start expanding the subarray to the right and repeat the process to find all subarrays with the required sum.

Python code for dynamic sliding window
```
def dynamic_sliding_window(arr: List[int], x:int):
    min_length = float('inf')
    start,end,current_sum = 0,0,0
    while(end < len(arr)):
        current_sum += arr[end]
        end += 1
        
        while(start < end and current_sum >= x):
            current_sum -= arr[start]
            start += 1
            min_length = min(min_length,end-start+1)
    return min_length
```
In this algorithm, we move through the array in sort of a caterpillar like movement. Expanding the window and then contracting.

## When to Use Sliding Window
Sliding window is useful where order of the elements of the initial array is important. For instance, the above algorithm will produce optimal solution for finding length of subarray that sums to 7 for the given input array [1,2,3,4,5,6]. However, if the input array is not sorted, we will still get the smallest window where the sum is 7 but we may not get the smallest number of elements that sum to 7. For example, for array [3,1,2,4], the smallest number of elements that sum to 7 is 2, i.e. 4 and 3. However, smallest subarray that sums to 7 is [1,2,4]. Other approaches like dynamic programming or two pointers are better suited if 
- Required subarrays are not contiguous.
- Relative order of elements is significant in the problem.

In my understanding, sliding window is a special case of two pointer pattern.

