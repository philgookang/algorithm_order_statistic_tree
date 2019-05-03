
class COLOR:
    RED     = "RED"
    BLACK   = "BLACK"

class Node:
    def __init__(self, **kwargs):
        self.key = kwargs["key"] if "key" in kwargs else None
        self.color = kwargs["color"] if "color" in kwargs else None
        self.left = kwargs["left"] if "left" in kwargs else None
        self.right = kwargs["right"] if "right" in kwargs else None
        self.size = kwargs["size"] if "size" in kwargs else 1
        self.parent = kwargs["parent"] if "parent" in kwargs else None

class RedBlackTree:

    def __init__(self):
        NIL = Node( key = "NIL", color = COLOR.BLACK, size = 0 )
        self.T = NIL
        self.NIL = NIL

    def find(self, x, i):
        if x == self.NIL:
            return self.NIL
        if x.key == i:
            return x
        elif i < x.key:
            return self.find(x.left, i)
        else:
            return self.find(x.right, i)

    def insert(self, z):
        y = self.NIL
        x = self.T
        while x != self.NIL:
            y = x
            y.size = y.size + 1             # just a guess
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.T = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z
        z.left = z.right = self.NIL
        z.color = COLOR.RED
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.parent != self.NIL and z.parent.color == COLOR.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y != self.NIL and y.color == COLOR.RED:
                    z.parent.color = COLOR.BLACK
                    y.color = COLOR.BLACK
                    z.parent.parent.color = COLOR.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = COLOR.BLACK
                    z.parent.parent.color = COLOR.RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == COLOR.RED:
                    z.parent.color = COLOR.BLACK
                    y.color = COLOR.BLACK
                    z.parent.parent.color = COLOR.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z) # might have to change this
                    z.parent.color = COLOR.BLACK
                    z.parent.parent.color = COLOR.RED
                    self.left_rotate(z.parent.parent) # might have to change this
        self.T.color = COLOR.BLACK

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.T = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

        y.size = x.size
        new_size = 0
        if x.left != self.NIL: new_size = new_size + x.left.size
        if x.right != self.NIL: new_size = new_size + x.right.size
        x.size = new_size + 1

    def left_rotate(self, x):
        y = x.right                   # set y
        x.right = y.left              # turn y's left subtree into x's right subtree
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent           # link x's parent to y
        if x.parent == self.NIL:
            self.T = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x                   # put x on y's left
        x.parent = y

        y.size = x.size
        new_size = 0
        if x.left != self.NIL: new_size = new_size + x.left.size
        if x.right != self.NIL: new_size = new_size + x.right.size
        x.size = new_size + 1

    def tree_minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def tree_successor(self, x):
        if x.right != self.NIL:
            return self.tree_minimum(x.right)
        y = x.parent
        while y != self.NIL and x == y.right:
            x = y
            y = y.parent
        return y

    def delete(self, i):

        z = self.find(self.T, i)
        y = None

        if z.left == self.NIL or z.right == self.NIL:
            y = z
        else:
            y = self.tree_successor(z)

        if y.left != self.NIL:
            x = y.left
        else:
            x = y.right

        x.parent = y.parent

        if y.parent == self.NIL:
            self.T = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != z:
            z.key = y.key

        if y.color == COLOR.BLACK:
            self.delete_fixup(x)

        return y

    def delete_fixup(self, x):
        while x != self.T and x.color == COLOR.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == COLOR.RED:
                    w.color = COLOR.BLACK
                    x.parent.color = COLOR.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == COLOR.BLACK and w.right.color == COLOR.BLACK:
                    w.color = COLOR.RED
                    x = x.parent
                    # x.parent = x.parent.parent
                else:
                    if w.right.color == COLOR.BLACK:
                        w.left.color = COLOR.BLACK
                        w.color = COLOR.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = COLOR.BLACK
                    w.right.color = COLOR.BLACK
                    self.left_rotate(x.parent)
                    x = self.T
            else:
                w = x.parent.left
                if w.color == COLOR.RED:
                    w.color = COLOR.BLACK                       # case 1
                    x.parent.color = COLOR.RED                  # case 1
                    self.right_rotate(x.parent)                 # case 1
                    w = x.parent.left                           # case 1
                if w.right.color == COLOR.BLACK and w.left.color == COLOR.BLACK:
                    w.color = COLOR.RED                         # case 2
                    x = x.parent                                # case 2
                    # x.parent = x.parent.parent
                else:
                    if w.left.color == COLOR.BLACK:
                        w.right.color = COLOR.BLACK             # case 3
                        w.color = COLOR.RED                     # case 3
                        self.left_rotate(w)                     # case 3
                        w = x.parent.left                       # case 3
                    w.color = x.parent.color                    # case 4
                    x.parent.color = COLOR.BLACK                # case 4
                    w.left.color = COLOR.BLACK                  # case 4
                    self.right_rotate(x.parent)                 # case 4
                    x = self.T                                  # case 4

        x.color = COLOR.BLACK

testcase = [
    { "insert" : [41, 38, 31, 12, 19, 8], "delete" : [ 8, 12, 19, 31, 38, 41 ] }
]


tree = RedBlackTree()

for case in testcase:
    for i in case["insert"]:
        tree.insert(Node(key = i))
        a = 1

    for i in case["delete"]:
        tree.delete(i)
        a = 2