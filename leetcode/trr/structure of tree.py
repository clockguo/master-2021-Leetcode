class bitree(object):
    def __init__(self,x=None):
        self.val=x
        self.left=None
        self.right = None


def isSubStructure(A,B):
    qe=[]
    qe.append(A)
    head = B
    def same(A,B):
        if B==None : return True
        if A==None or B.val!=A.val: return False
        return same(A.left,B.left) and same(A.right,B.right)
    ans = 0
    while len(qe):
        if qe[0].left:
            qe.append(qe[0].left)
        if qe[0].right:
            qe.append(qe[0].right)
        if qe[0].val==head.val:
            ans = same(qe[0],B)

        qe.remove(qe[0])
        if ans:return True
    return False

A = [1,2,3]
B = [3,1]
print(isSubStructure(A,B))

