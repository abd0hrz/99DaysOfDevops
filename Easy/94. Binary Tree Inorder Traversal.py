
class Solution(object):


    def inorderTraversal(self, root):
        if root is None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            if not isinstance(curr, TreeNode):
                res.append(curr)
                continue
            if curr.right is not None:
                stack.append(curr.right)
            stack.append(curr.val)
            if curr.left is not None:
                stack.append(curr.left)
        return res


