class ListNode(object):
    def __int__(self,x):
        self.val = x
        self.next=None

class List_handle:
    def __init__(self):
        self.cur_node = None

    def add(self,data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def print_ListNode(self, node):
        while node:
            print('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            node = node.next


    def reversePrint(self, head):
        res = []
        while head:
            res.append(head.val)
            head=head.next
        return res[::-1]

ListNode_1=List_handle()
# L1=ListNode()
head=[1,3,2]
for i in head:
    l1=ListNode_1.add(i)
List_handle().print_ListNode(l1)
res = ListNode_1.reversePrint(l1)
print(res)
