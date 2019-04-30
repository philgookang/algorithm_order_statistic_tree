
class COLOR:
    RED     = 1
    BLACK   = 2

class Node:
    def __init__(self, **kwargs):
        self.key = kwargs["key"] if "key" in kwargs else None
        self.color = kwargs["color"] if "color" in kwargs else None
        self.left = kwargs["left"] if "left" in kwargs else None
        self.right = kwargs["right"] if "right" in kwargs else None
        self.size = kwargs["size"] if "size" in kwargs else None
        self.root = kwargs["root"] if "root" in kwargs else None
        self.parent = kwargs["parent"] if "parent" in kwargs else None

class RedBlackTree:

    def __init__(self):
        self.T = None
        self.NIL = None

    def insert(self, z):
        y = self.NIL
        x = self.T
        while x != self.NIL:
            y = x
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
        while z.parent.color == COLOR.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == COLOR.RED:
                    z.parent.color = COLOR.BLACK
                    y.color = COLOR.BLACK
                    z.parent.parent.color = COLOR.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = COLOR.BLACK
                    z.parent.parent.color = COLOR.BLACK
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
                    z.parent.parent.color = COLOR.BLACK
                    self.right_rotate(z.parent.parent) # might have to change this
        self.T.color = COLOR.BLACK

    def right_rotate(self, z):
        pass

    def left_rotate(self, z):
        pass

    def tree_successor(self, z):
        pass

    def delete_fixup(self, x):
        pass

    def delete(self, z):

        y = x = None

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
        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x

        if y != z:
            z.key = y.key

        if y.color == COLOR.BLACK:
            self.delete_fixup(x)

        return y



a = Node(key = "John")
b = Node(key = "Kim")

c = a

if a == b:
    print("a == b")
else:
    print("a != b")

if a == c:
    print("a == c")
else:
    print("a != c")



# rbTree = RedBlackTree()