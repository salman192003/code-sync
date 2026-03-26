# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def dfs (node,total):
            if not node:
                return False

            total = total - node.val

            if total == 0 and node.left == None and node.right == None:
                return True

            return dfs(node.left,total) or dfs(node.right,total)



        return dfs(root,targetSum)