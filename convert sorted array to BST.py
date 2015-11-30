'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        root = self.construct(0, len(nums) - 1)
        return root
        
    def construct(self, start, end):
        if start == end:
            return TreeNode(self.nums[start])
        if start > end:
            return None
        mid = (start + end) / 2 # find middle number of subarray as root recursively
        root = TreeNode(self.nums[mid])
        root.left = self.construct(start, mid - 1)
        root.right = self.construct(mid + 1, end)
        return root
