def levelOrder(root):
    if not root: return []
    qeuen = []
    ans = []
    tips = []
    anst = []
    qeuen.append(root)
    tips.append(0)
    while len(qeuen):
        ans.append(qeuen[0].val)
        anst.append(tips[0].val)
        if qeuen[0].left:
            qeuen.append(qeuen[0].left)
            tips.append(tips[0]+1)
        if qeuen[0].right:
            qeuen.append(qeuen[0].right)
            tips.append(tips[0]+1)
        qeuen.remove(qeuen[0])
        tips.remove(tips[0])
    print(tips)
    return ans
