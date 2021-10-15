class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.X = []

    def push(self, x):
        self.X.insert(0,x)

    def pop(self):
        self.X.remove(self.X[0])
    def top(self):
        return self.X[0]
    def min(self):
        return min(self.X[:])
minstack = MinStack()
minstack.push(2)
minstack.push(4)
minstack.push(0)
print(minstack.min())
minstack.pop()
print(minstack.min())
print(minstack)

