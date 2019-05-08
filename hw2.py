
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

# A simple tree recursive search method
def find(x, i):
    global l, NIL

    if x == NIL:
        return NIL
    if x.key == i:
        return x
    elif i < x.key:
        return find(x.left, i)
    else:
        return find(x.right, i)

# CLRS textbook RIGHT-ROTATE pseudocode
# page: 278 ".. The code for RIGHT-ROTATE is symmetric..."
def right_rotate(x):
    global l, NIL

    y = x.left
    x.left = y.right
    if y.right != NIL:
        y.right.parent = x
    y.parent = x.parent
    if x.parent == NIL:
        l = y
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
def left_rotate(x):
    global l, NIL

    y = x.right  # set y
    x.right = y.left  # turn y's left subtree into x's right subtree
    if y.left != NIL:
        y.left.parent = x
    y.parent = x.parent  # link x's parent to y
    if x.parent == NIL:
        l = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x  # put x on y's left
    x.parent = y

    # CLRS Dynamic Order Statistics
    # page: 306    "size[x] = size[left[x]] + size[right[x]] + 1"
    y.size = x.size
    x.size = x.left.size + x.right.size + 1

# CLRS textbook RB-INSERT pseudocode
# page: 280
def insert_fixup(z):
    global l, NIL

    while z.parent != NIL and z.parent.color == COLOR.RED:
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y != NIL and y.color == COLOR.RED:
                z.parent.color = COLOR.BLACK
                y.color = COLOR.BLACK
                z.parent.parent.color = COLOR.RED
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    left_rotate(z)
                z.parent.color = COLOR.BLACK
                z.parent.parent.color = COLOR.RED
                right_rotate(z.parent.parent)
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
                    right_rotate(z)
                z.parent.color = COLOR.BLACK
                z.parent.parent.color = COLOR.RED
                left_rotate(z.parent.parent)
    l.color = COLOR.BLACK

# CLRS textbook TREE-MINIMUM pseudocode
# page: 258
def tree_minimum( x):
    global l, NIL

    while x.left != NIL:
        x = x.left
    return x

# CLRS textbook TREE-SUCCESSOR pseudocode
# page: 259
def tree_successor(x):
    global l, NIL

    if x.right != NIL:
        return tree_minimum(x.right)
    y = x.parent
    while y != NIL and x == y.right:
        x = y
        y = y.parent
    return y

# CLRS textbook RB-DELETE-FIXUP pseudocode
# page: 289
def delete_fixup(x):
    while x != l and x.color == COLOR.BLACK:
        if x == x.parent.left:
            w = x.parent.right
            if w.color == COLOR.RED:
                w.color = COLOR.BLACK                       # case 1
                x.parent.color = COLOR.RED                  # case 1
                left_rotate(x.parent)                       # case 1
                w = x.parent.right                          # case 1
            if w.left.color == COLOR.BLACK and w.right.color == COLOR.BLACK:
                w.color = COLOR.RED                         # case 2
                x = x.parent                                # case 2
            else:
                if w.right.color == COLOR.BLACK:
                    w.left.color = COLOR.BLACK              # case 3
                    w.color = COLOR.RED                     # case 3
                    right_rotate(w)                         # case 3
                    w = x.parent.right                      # case 3
                w.color = x.parent.color                    # case 4
                x.parent.color = COLOR.BLACK                # case 4
                w.right.color = COLOR.BLACK                 # case 4
                left_rotate(x.parent)                       # case 4
                x = l                                       # case 4
        else:
            w = x.parent.left
            if w.color == COLOR.RED:
                w.color = COLOR.BLACK                       # case 1
                x.parent.color = COLOR.RED                  # case 1
                right_rotate(x.parent)                      # case 1
                w = x.parent.left                           # case 1
            if w.right.color == COLOR.BLACK and w.left.color == COLOR.BLACK:
                w.color = COLOR.RED                         # case 2
                x = x.parent                                # case 2
            else:
                if w.left.color == COLOR.BLACK:
                    w.right.color = COLOR.BLACK             # case 3
                    w.color = COLOR.RED                     # case 3
                    left_rotate(w)                          # case 3
                    w = x.parent.left                       # case 3
                w.color = x.parent.color                    # case 4
                x.parent.color = COLOR.BLACK                # case 4
                w.left.color = COLOR.BLACK                  # case 4
                right_rotate(x.parent)                      # case 4
                x = l                                       # case 4
    x.color = COLOR.BLACK

#
# ##################################################################
#

def init():
    global l
    global cnt
    # l = []

    # Sentinel nil[T] object
    global NIL
    NIL = Node(key="NIL", color=COLOR.BLACK, size=0)
    l = NIL

# noinspection PyUnresolvedReferences
def os_insert(i):
    global l, NIL

    if NIL != find(l, i):
        return 0

    z = Node(key=i)
    y = NIL
    x = l
    while x != NIL:
        y = x
        y.size = y.size + 1  # CLRS Dynamic Order Statistics : "..increment size[x] for each node on the path traversed from the root down toward the leaves.."
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == NIL:
        l = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    z.left = z.right = NIL
    z.color = COLOR.RED
    insert_fixup(z)

    return i

# CLRS textbook RB-DELETE pseudocode
# page: 288
# noinspection PyUnresolvedReferences
def os_delete(i):
    global l, NIL

    z = find(l, i)

    if z == NIL:
        return 0

    y = None

    if z.left == NIL or z.right == NIL:
        y = z
    else:
        y = tree_successor(z)

    if y.left != NIL:
        x = y.left
    else:
        x = y.right

    x.parent = y.parent

    if y.parent == NIL:
        l = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    if y != z:
        z.key = y.key

    # CLRS Dynamic Order Statistics
    # page: 307 "...traverse a path from node y up to the root, decrementing the size field of each node on the path.."
    backprop = y.parent
    while backprop != NIL:
        backprop.size = backprop.size - 1
        backprop = backprop.parent

    if y.color == COLOR.BLACK:
        delete_fixup(x)

    return i

# CLRS textbook OS-SELECT pseudocode
    # page: 304
def os_select(i):
    global l, NIL

    def recursive_select(x, i):
        global l, NIL

        if x == NIL:
            return 0
        r = x.left.size + 1
        if i == r:
            return x.key      # change this to return value not node
        elif i < r:
            return recursive_select(x.left, i)
        else:
            return recursive_select(x.right, i - r)

    return recursive_select(l, i)

# CLRS textbook OS-RANK pseudocode
# page: 305
def os_rank(i):
    global l, NIL

    # find node
    x = find(l, i)

    # check if node is found
    if x == NIL:
        return 0

    r = x.left.size + 1
    y = x

    while y != l:
        if y == y.parent.right:
            r = r + y.parent.left.size + 1
        y = y.parent

    return r

def check(opt_seq,in_seq,out_seq):
    h = {  }
    init()
    for opt,val,ans in zip(opt_seq,in_seq,out_seq):
        if opt==0:
            h[val] = 1
            if os_insert(val)!=ans:
                return False
        elif opt==1:
            if os_delete(val)!=ans:
                return False
        elif opt==2:
            if os_select(val)!=ans:
                return False
        else:
            if os_rank(val)!=ans:
                return False
    return True


