class Solution:
    def getKthFromLast(self, head, k):

        first = head
        second = head

        # Move first pointer k steps ahead
        for i in range(k):
            if first is None:
                return -1
            first = first.next

        # Move both pointers together
        while first:
            first = first.next
            second = second.next

        return second.data