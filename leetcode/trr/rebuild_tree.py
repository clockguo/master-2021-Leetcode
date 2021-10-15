class bitree(object):
    def __init__(self,x=None):
        self.val = x
        self.lchild = None
        self.rchild = None

class bitree_handle:
    def __init__(self):
        self.cur_node = None

    def rebuildTree(self,preorder,inorder):
        if len(inorder)==0 or len(preorder)==0:
            return None
        self.pre,self.in_dic=preorder,{}
        for i in range(len(inorder)):
            self.in_dic[inorder[i]] = i
        num = self.in_dic[preorder[0]]
        node=bitree()
        node.val = preorder[0]
        node.lchild=bitree_handle.rebuildTree(self,preorder[1:num+1],inorder[:num])
        node.rchild=bitree_handle.rebuildTree(self,preorder[num+1:],inorder[num+1:])
        return node

    def TreePrint(self,head):
        row_order=[]
        queue = []
        queue.append(head)
        while len(queue):
            # if queue==[]:
            #     break
            row_order.append(queue[0].val)
            frist_t = queue[0]
            if frist_t.lchild != None:
                queue.append(frist_t.lchild)
            if frist_t.rchild != None:
                queue.append(frist_t.rchild)
            queue.remove(frist_t)
        return row_order

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# inorder = []
Lo = bitree_handle()
opo = Lo.rebuildTree(preorder,inorder)
print(Lo.TreePrint(opo))

print(opo)

