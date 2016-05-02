class Solution(object):
    """
    Two ways to do it. First way, is to sort the list first, take the first element and find the next element using binary search. nlogn.
    Second way: put in hashmap, but before putting, see if target - n is present in map. extra n space. O(n) time.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numIndexDict = {}
        for i in range(0, len(nums)):
            value = target - nums[i]
            if value in numIndexDict:
                return (i, numIndexDict[value])
            numIndexDict[nums[i]] = i
