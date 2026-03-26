# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        def is_leaf(node):
            if node.left or node.right:
                return False
            else:
                return True

        result = []

        def dfs(node,path,total):

            if not node:
                return

            path.append(node.val)

            total = total - node.val

            if total == 0 and is_leaf(node):
                result.append(path[:])

            dfs(node.left,path,total)
            dfs(node.right,path,total)

            path.pop()

        summation = targetSum
        dfs(root,[],summation)
        

        return result