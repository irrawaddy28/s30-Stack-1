'''
503 Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/description/

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]

Example 3:
Input: nums = [9,8,7,6,5]
Output: [-1,9,9,9,9]

Constraints:
1 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9

Solution
1. Brute Force
Run two nested loops. The outer loop fixes the reference element, the inner loop searches for the next greater element.
https://www.youtube.com/watch?v=sK5YcQAed5k
Time: O(N^2), Space: O(1)

2. Monotonic Increasing Stack
We go through the array twice to simulate the circular nature.
For each number in nums array, we use a stack to track the next greater element efficiently. As soon as we find a bigger one, we update and move on, skipping repeated work. It's easier to understand through the lecture link below.
https://youtu.be/sK5YcQAed5k?t=399 (6:44-21:00)
Time: O(N), Space: O(N)

'''
from typing import List

# lecture solution
def nextGreaterElements(nums: List[int]) -> List[int]:
    N = len(nums)
    stack = [0] # index of first element in nums
    result = [-1]*N
    for i in range(1,2*N): # two iterations over nums
        next_element = nums[i % N]

        # As long as next element is greater than top of stack
        # keep popping the top
        while stack and next_element > nums[stack[-1]]:
            # Note: stack[-] = stack.top() = stack.peek()
            index = stack.pop()
            result[index] = next_element

        # Push the index of next element to the stack but ...
        # push only the indices from the 1st iteration (over nums)
        # because pushing the same indices in the 2nd iter will result
        # in duplication, i.e., 'result' array will be repopulated with the
        # same values
        if i < N:
            stack.append(i)
    return result

# my solution
# def nextGreaterElements(nums: List[int]) -> List[int]:
#     N = len(nums)
#     stack = [0] # index of first element in nums
#     result = [-1]*N
#     filled = [False]*N
#     for i in range(1,2*N+1):
#         num = nums[i % N]
#         while stack and num > nums[stack[-1]]:
#             j = stack.pop()
#             if not filled[j]:
#                 result[j] = num
#                 filled[j] = True
#         if not filled[i%N]:
#             stack.append(i%N)
#     return result

def run_nextGreaterElements():
    tests = [([1,2,3,4,3], [2,3,4,-1,4]),
             ([9,8,7,6,5],[-1,9,9,9,9]),
             ([1,2,1],[2,-1,2]),
    ]
    for test in tests:
        nums, ans = test[0], test[1]
        result = nextGreaterElements(nums)
        print(f"\nnums= {nums}")
        print(f"next greater elements = {result}")
        success = (ans == result)
        print(f"Pass: {success}")
        if not success:
            print(f"Failed")
            return

run_nextGreaterElements()
