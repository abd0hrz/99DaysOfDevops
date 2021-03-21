class Solution(object):

    def deleteDuplicates(self, head):
        if head is None:
            return None
        pos = head
        while pos is not None and pos.next is not None:
            if pos.val == pos.next.val:
                pos.next = pos.next.next
            else:
                pos = pos.next
        return head
