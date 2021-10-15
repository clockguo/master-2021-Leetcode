class Tree():
    def __init__(self,x=None):
        self.val = x
        self.left = None
        self.right = None


def flatten(head): #将二叉树摊平
    prelist = []
    def prefind(head):
        if not head: return
        prelist.append(head)
        prefind(head.left)
        prefind(head.right)
    N = len(prelist)
    i = 0
    while i<N:
        j = i+1
        prelist[i].left = None
        if j<N:
            prelist[i].right = prelist[j]
        else: prelist[i].right = None
    return prelist[0]

