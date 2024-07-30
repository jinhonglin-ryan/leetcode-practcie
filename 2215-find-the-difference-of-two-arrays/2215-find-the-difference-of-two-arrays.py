class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        ans1 = set()
        ans2 = set()
        
        num2set = set(nums2)
        num1set = set(nums1)
        
        for num in nums1:
            if num not in num2set:
                ans1.add(num)
                
        for num in nums2:
            if num not in num1set:
                ans2.add(num)
                
        ans.append(list(ans1))
        ans.append(list(ans2))
        
        return ans 