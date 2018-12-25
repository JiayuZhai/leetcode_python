class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def maxIndex(nums,start,end):
            maxI = start
            for i in range(start,end+1):
                if nums[i]>nums[maxI]:
                    maxI = i
            return maxI
        
        def buildTree(nums, start ,end):
            if start>end:
                return None
            maxI = maxIndex(nums, start, end)
            root = TreeNode(nums[maxI])
            root.left = buildTree(nums,start,maxI-1)
            root.right = buildTree(nums,maxI+1,end)
            return root
        
        
        return buildTree(nums,0,len(nums)-1)
