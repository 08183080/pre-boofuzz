"""
i want to get a tree
"""

s1 = [1, 0, 2]
s2 = [1, 0, 3]
s3 = [1, 0, 4, 5]

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.n1 = None
        self.n2 = None
        self.n3 = None


    def add(self, l: list):
        n = len(l)
        # self.value = l[0]
        for i in range(1, n):
            if self.n1 and self.n1.value == l[i]:
                break
            elif self.n2 and self.n2.value == l[i]:
                break
            elif self.n3 and self.n3.value == l[i]:
                break
            elif self.n1 == None:
                self.n1.value = l[i]
            elif self.n1 and self.n2 == None:
                self.n2.value = l[i]
            else:
                self.n3.value = l[i]         


if __name__ == "__main__":
    t = TreeNode(1)
    t.add(s1)
    # t.n1 = TreeNode(0)
    # t.n1.n1 = TreeNode(2)
    # t.n1.n2 = TreeNode(3)
    # t.n1.n3 = TreeNode(4)
    # t.n1.n3.n1 = TreeNode(5)
    

