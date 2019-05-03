
class COLOR:
    RED     = "RED"
    BLACK   = "BLACK"

class Node:
    def __init__(self, **kwargs):
        self.key        = kwargs["key"]     if "key"         in kwargs else None
        self.color      = kwargs["color"]   if "color"      in kwargs else None
        self.left       = kwargs["left"]    if "left"       in kwargs else None
        self.right      = kwargs["right"]   if "right"      in kwargs else None
        self.size       = kwargs["size"]    if "size"       in kwargs else 1
        self.parent     = kwargs["parent"]  if "parent"     in kwargs else None

class RedBlackTree:

    def __init__(self):

        # Sentinel nil[T] object
        NIL = Node( key = "NIL", color = COLOR.BLACK, size = 0 )

        # pointer to root node
        self.T = NIL

        # sentinel object
        self.NIL = NIL

    # CLRS textbook partition pseudocode
    # page: 147
    def find(self, x, i):
        if x == self.NIL:
            return self.NIL
        if x.key == i:
            return x
        elif i < x.key:
            return self.find(x.left, i)
        else:
            return self.find(x.right, i)

    # CLRS textbook RB-INSERT-FIXUP pseudocode
    # page: 281
    def insert(self, z):
        y = self.NIL
        x = self.T
        while x != self.NIL:
            y = x
            y.size = y.size + 1    # CLRS Dynamic Order Statistics : "..increment size[x] for each node on the path traversed from the root down toward the leaves.."
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

    # CLRS textbook RB-INSERT pseudocode
    # page: 280
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

    # CLRS textbook RIGHT-ROTATE pseudocode
    # page: 278 ".. The code for RIGHT-ROTATE is symmetric..."
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

        # CLRS Dynamic Order Statistics
        # page: 306    "size[x] = size[left[x]] + size[right[x]] + 1"
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    # CLRS textbook LEFT-ROTATE pseudocode
    # page: 278
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

        # CLRS Dynamic Order Statistics
        # page: 306    "size[x] = size[left[x]] + size[right[x]] + 1"
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    # CLRS textbook TREE-MINIMUM pseudocode
    # page: 258
    def tree_minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    # CLRS textbook TREE-SUCCESSOR pseudocode
    # page: 259
    def tree_successor(self, x):
        if x.right != self.NIL:
            return self.tree_minimum(x.right)
        y = x.parent
        while y != self.NIL and x == y.right:
            x = y
            y = y.parent
        return y

    # CLRS textbook RB-DELETE pseudocode
    # page: 288
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

        # CLRS Dynamic Order Statistics
        # page: 307 "...traverse a path from node y up to the root, decrementing the size field of each node on the path.."
        backprop = y.parent
        while backprop != self.NIL:
            backprop.size = backprop.size - 1
            backprop = backprop.parent

        if y.color == COLOR.BLACK:
            self.delete_fixup(x)

        return y

    # CLRS textbook RB-DELETE-FIXUP pseudocode
    # page: 289
    def delete_fixup(self, x):
        while x != self.T and x.color == COLOR.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == COLOR.RED:
                    w.color = COLOR.BLACK                       # case 1
                    x.parent.color = COLOR.RED                  # case 1
                    self.left_rotate(x.parent)                  # case 1
                    w = x.parent.right                          # case 1
                if w.left.color == COLOR.BLACK and w.right.color == COLOR.BLACK:
                    w.color = COLOR.RED                         # case 2
                    x = x.parent                                # case 2
                else:
                    if w.right.color == COLOR.BLACK:
                        w.left.color = COLOR.BLACK              # case 3
                        w.color = COLOR.RED                     # case 3
                        self.right_rotate(w)                    # case 3
                        w = x.parent.right                      # case 3
                    w.color = x.parent.color                    # case 4
                    x.parent.color = COLOR.BLACK                # case 4
                    w.right.color = COLOR.BLACK                 # case 4
                    self.left_rotate(x.parent)                  # case 4
                    x = self.T                                  # case 4
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

if __name__ == "__main__":

    testcase = [
        { "insert" : [41, 38, 31, 12, 19, 8], "delete" : [ 8, 12, 19, 31, 38, 41 ] }
    ]

    tree = RedBlackTree()

    for case in testcase:
        for i in case["insert"]:
            tree.insert(Node(key = i))

        for i in case["delete"]:
            tree.delete(i)