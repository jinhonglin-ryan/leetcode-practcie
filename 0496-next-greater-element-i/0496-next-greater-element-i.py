class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # 单调栈
        # 在nums2找一个数的右边的第一个最大的数
        # 保持从栈头到栈尾递增的栈，遍历nums2，加入索引
        ans = [-1 for _ in range(len(nums1))]
    
        umap = {}
        # 建立数组1，数字到index的dictionary
        for i in range(len(nums1)):
            umap[nums1[i]] = i
            
        stack = [0]
        for i in range(1, len(nums2)):
            
            # 如果当前数字小于等于当前栈头，加入单调栈，维持递增
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            
            # 如果当前数字大于栈头，需要移除栈中比当前数字小的那些数
            else:
                while stack and nums2[i] > nums2[stack[-1]]:
                    # 如果当前栈头在umap中，说明当前nums[i]为当前栈头对应的index在nums2中的下一个大大数，需要更新到ans
                    if nums2[stack[-1]] in umap:
                        num = nums2[i]
                        index = umap[nums2[stack[-1]]]
                        ans[index] = num
                    stack.pop()
                
                # 循环完成后，nums[i] < nums[stack[-1]]，所以需要加入stack
                stack.append(i)
                
        return ans
                
                    
     
        