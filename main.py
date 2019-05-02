
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
        self.T = None
        self.NIL = None

    def select(self, x, i):
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.select(x.left, i)
        else:
            return self.select(x.right, i - r)

    def rank(self, x):
        r = x.left.size + 1
        y = x
        while y != self.T:
            if y == y.parent.right:
                r = r + y.parent.left.size + 1
            y = y.parent
        return r

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
        z.left = self.NIL
        z.right = self.NIL
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
                        self.left_rotate(z) # might have to change this
                    z.parent.color = COLOR.BLACK
                    z.parent.parent.color = COLOR.RED
                    self.right_rotate(z.parent.parent) # might have to change this
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

    def delete_fixup(self, x, y):
        father = y.parent
        while x != self.T and (x == self.NIL or x.color == COLOR.BLACK):
            if x == father.left:
                w = father.right
                if w == self.NIL:
                    x = self.T
                else:
                    if w.color == COLOR.RED:
                        w.color = COLOR.BLACK
                        father.color = COLOR.RED
                        self.left_rotate(father)    # father
                        continue
                    if (w.left == self.NIL or w.left.color == COLOR.BLACK) and \
                            (w.right == self.NIL or w.right.color == COLOR.BLACK):
                        w.color = COLOR.RED
                        x = father
                        father = x.parent
                    else:
                        if w.right == self.NIL or  w.right.color == COLOR.BLACK:
                            if w.left != self.NIL:
                                w.left.color = COLOR.BLACK
                                w.color = COLOR.RED
                                self.right_rotate(father)    # w
                                w = father.right
                        w.color = father.color
                        father.color = COLOR.BLACK
                        if w.right != self.NIL:
                            w.right.color = COLOR.BLACK
                        self.left_rotate(father)    # father
                        x = self.T
            else:
                w = father.left
                if w == self.NIL:
                    x = self.T
                else:
                    if w.color == COLOR.RED:
                        w.color = COLOR.BLACK
                        father.color = COLOR.RED
                        self.right_rotate(father) # father
                        continue
                    if (w.left == self.NIL or w.left.color == COLOR.BLACK) and \
                            (w.right == self.NIL or w.right.color == COLOR.BLACK):
                        w.color = COLOR.RED
                        x = father
                        father = x.parent
                    else:
                        if w.left == self.NIL or w.left.color == COLOR.BLACK:
                            if w.right != self.NIL:
                                w.right.color = COLOR.BLACK
                                w.color = COLOR.RED
                                self.left_rotate(father)   # w
                                w = father.left
                        w.color = father.color
                        father.color = COLOR.BLACK
                        if w.left != self.NIL:
                            w.left.color = COLOR.BLACK
                        self.right_rotate(father)   # father
                        x = self.T

        if x != self.NIL:
            x.color = COLOR.BLACK

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.T = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, i):

        z = self.find(self.T, i)

        # does not exists
        if z == self.NIL:
            return 0

        # ==========================

        y = x = None

        if z.left == self.NIL or z.right == self.NIL:
            y = z
        else:
            y = self.tree_successor(z)

        if z.left != self.NIL:
            x = y.left
        else:
            x = y.right

        if x != self.NIL:
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
            self.delete_fixup(x, y)


        return y

lst = [41, 38, 31, 12, 19, 8]
# lst = [26, 17, 41, 14, 21,30, 47, 10, 16, 19, 21, 28, 38, 7, 12, 14, 20, 35, 39, 3]
tree = RedBlackTree()

for i in lst:
    tree.insert(Node(key = i))

tree.delete( 19 )

tree.delete( 12 )

if len(lst) == 3:
    print("hello")