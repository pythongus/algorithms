# Given a list of sorted linked lists, merge them into one list in order
# For example:
# input: [[1,2,3], [2,3,4], [5,6]]
# result: [1,2,2,3,3,4,5,6]


class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None


def merge_sorted_linked_lists(lists):
    """
    :param arrays: List[ListNode]
    :return ListNode
    """
    def get_next(head):
        min_val = None
        index = -1
        for ind, hd in enumerate(lists):
            if hd and not (min_val and min_val <= hd.val):
                min_val = hd.val
                index = ind

        if index >= 0:
            min_head, lists[index] = lists[index], lists[index].next
            if head:
                head.next = min_head
            else:
                head = min_head

            return head

        return None

    head = get_next(None)
    h = head
    while head:
        head = get_next(head)
        if head:
            head = head.next

    return h


def linked_list_values(head):
    r = []
    while head:
        r.append(head.val)
        head = head.next
    return r


def test_nodes():
    a = ListNode(2)
    a.next = ListNode(3)
    a.next.next = ListNode(4)
    lists = [a]

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    lists.append(a)

    a = ListNode(5)
    a.next = ListNode(6)
    lists.append(a)
    assert (linked_list_values(merge_sorted_linked_lists(lists)) == [1, 2, 2, 3, 3, 4, 5, 6])
