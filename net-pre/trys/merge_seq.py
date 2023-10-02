"""
尝试写个demo例子,对于多序列进行合并的demo       2023/9/30


"""

s1 = [1,0,2]
s2 = [1,0,3]
s3 = [1,0,4,5]
# s3 = [1,0,2,3,4]
s = [s1, s2, s3]

"""
看,合并策略可以有多种...
    root(None)                                  
         |   
         1
    /          \
    0          3
   / \          \
   2  3         4               


       root(None)
         |   
         1
        /          
        0          
    / \          
    2  3        
         \
            4
"""


"""
假设序列中没有重复的请求,每一个都是标准的,每一个都是unique的...
"""
class TreeNode:
    def __init__(self, value):
        self.value = value  # 结点的值
        self.children = []  # 结点的孩子节点
        

    def merge_sequences(self, seqs):
        # 将序列合并到树中
        root = TreeNode(-1)
        value2node = {}

        # 结点出来了,接下来就是将结点加入树中了...
        for s in seqs:
            cur = root
            for i in s:
                if i in value2node:
                    child = value2node[i]
                else:
                    child = TreeNode(i)
                    value2node[i] = child


                # 先判断新节点是否存在,然后在确定是否加入
                exist = None
                for node in cur.children:
                    if node.value == child.value:
                        exist = node
                        # continue
                
                if exist:
                    cur = exist
                else:
                    cur.children.append(child)
                    print("添加",child.value)
                    cur = child
                
        return root

    def print_tree(self, node, indent=""):
        if node.value != -1:  # 不打印根节点的值为 -1 的情况
            print(indent + str(node.value))
        for child in node.children:
            self.print_tree(child, indent + "  ")



root = TreeNode(None)
root = root.merge_sequences(s)
root.print_tree(root)
# root.traverse()
print("~~~")









