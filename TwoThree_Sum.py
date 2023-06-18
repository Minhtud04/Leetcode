import random
'''
LeetCode 1: Two SUm
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
def twoSum(nums: list, target)->list:
    #Using hashmap
    '''
    Brute Force:
        1. Give 2 pointers - run through => n!
    How to do it 1 pass:
            Run through -> store target- dic[i] as key
            Check if nums[i] in dic or not.
    '''
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[target - nums[i]] = i
        else:
            return [i, dic[nums[i]]]
    return []

def testGen2Sum(length: int)-> tuple:
    target = random.randint(0,20)
    lis = []
    for i in range(length):
        lis.append(random.randint(0,25))

    return (lis, target)
def test_TwoSum():
    for i in range(10):
        tup: tuple = testGen2Sum(10)
        print(f"Test case {i}: {tup}")
        print(twoSum(*tup))

#===================================================

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
'''

def threeSum()