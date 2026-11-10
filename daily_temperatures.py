'''
739 Daily Temperatures
https://leetcode.com/problems/daily-temperatures/description/

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

Solution:
1. Brute Force
Go through each temperature one by one. For each temperature, we look ahead to find a warmer day. Once we find it, we note how many days it took, and move on.
https://youtu.be/HN7Vy27zDZY?t=191
Time: O(N^2), Space: O(1)

2. Monotonic Increasing Stack
Use a stack to keep track of indices where we haven't found a warmer day yet.
For each temperature, if it's warmer than the one at the top of the stack, we found our answer for that earlier day. We keep doing this until we handle all temperatures one by one.
https://youtu.be/HN7Vy27zDZY?t=400
Time: O(N), Space: O(N)
'''
from typing import List

# works
# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#     if not temperatures:
#         return []
#     N = len(temperatures)
#     result = [0]*N
#     stack = [0] # index of first element in nums
#     for i in range(1, N):
#         next_temp = temperatures[i]
#         while stack and next_temp > temperatures[stack[-1]]:
#             j = stack.pop()
#             result[j] =  i - j
#         stack.append(i)
#     return result

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    if not temperatures:
        return []
    N = len(temperatures)
    result = [0]*N
    peek = -1
    stack = [(0, temperatures[0])] # (index, temperature) of first element in  nums
    for i in range(1, N):
        next_temp = temperatures[i]
        while stack and stack[peek][1] < next_temp:
            [j, prev_temp] = stack.pop()
            result[j] = i - j
        stack.append((i, next_temp))
    return result

def run_tests():
    tests = [([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
             ([30,40,50,60],[1,1,1,0]),
             ([30,60,90],[1,1,0]),
             ([78,76,74,72,70,69,65],[0,0,0,0,0,0,0]),
             ([25],[0]),
             ([25,35],[1,0]),
    ]
    for test in tests:
        temperatures, ans = test[0], test[1]
        result = dailyTemperatures(temperatures)
        print(f"\ntemperatures = {temperatures}")
        print(f"num days to warmer day = {result}")
        passed = (ans == result)
        assert passed == True, f"Test case failed"
        print(f"Pass: {passed}")
    print(f"\nDONE")

run_tests()
