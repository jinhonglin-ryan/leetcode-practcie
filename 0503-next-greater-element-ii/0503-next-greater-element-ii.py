class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # 单调栈
        # 思路：把nums复制一遍，然后找右边的第一个更大的值即可，维护一个从栈头到栈尾递增的单调栈
        # 最后保留res的前len(nums)长度
        
        arr = [0] * len(nums) * 2
        
        for i in range(len(nums)):
            arr[i] = nums[i]
        
        for i in range(len(nums)):
            arr[i + len(nums)] = nums[i]
        
        res = [-1] * len(arr)
        
        stack = []
        
        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                index = stack[-1]
                res[index] = arr[i]
                stack.pop()
            
            stack.append(i)
            
        
        return res[:len(nums)]
                
        
            
        
        