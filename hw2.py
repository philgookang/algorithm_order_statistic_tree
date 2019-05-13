import random

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

    A = []

    # Checker program array insert
    def checker_insert(array, val):
        if val in array: return 0
        array.append(val)
        return val

    # Checker program array delete
    def checker_delete(array, val):
        if val in array:
            array.remove(val)
            return val
        return 0

    # Checker program check rank
    def checker_rank(A, x):
        A = A.copy()
        location = -1
        A.sort()
        for ind, val in enumerate(A):
            if x == A[ind]:
                location = ind
                break

        # 못 찾았으면 0
        if location == -1: return 0

        # 아니면 실째 위띵
        return location + 1

    # Checker program select
    def checker_select(A, val):

        # CLRS textbook partition pseudocode
        # page: 147
        def Partition(A, p, r):
            x = A[r]  # select pivot as the last element in list
            i = p - 1  # get starting position
            for j in range(p, r):
                if A[j] <= x:  # check current value is smaller than pivot
                    i = i + 1
                    A[i], A[j] = A[j], A[i]  # switch location
            A[i + 1], A[r] = A[r], A[i + 1]  # move pivot to correct location
            return i + 1

        # CLRS textbook randomized partition pseudocode
        # page: 154
        def RandomPartition(A, p, r):
            # select a random position as pivot
            try:
                i = random.randint(p, r)
            except ValueError:
                i = random.randint(r, p)
            A[i], A[r] = A[r], A[i]  # send pivot to last location in array

            # sort by pivot
            return Partition(A, p, r)

        # CLRS textbook randomized select pseudocode
        # page: 186
        def RandomSelect(A, p, r, i):

            # check if i is inside array len
            if i > len(A):
                return 0

            # if only one in the array return it
            if p == r:
                return A[r]

            # get a random index
            q = RandomPartition(A, p, r)

            # check if we have found item
            # i = k what we have found is equal to search then return
            # i < k what we have found is larger then search between p to q
            # i > k what we have found is larger then search between q to r
            k = q - p + 1
            if i == k:
                return A[q]
            elif i < k:
                return RandomSelect(A, p, q - 1, i)
            else:
                return RandomSelect(A, q + 1, r, i - k)

        return RandomSelect(A.copy(), 0, (len(A) - 1), val)

    for opt,val,ans in zip(opt_seq,in_seq,out_seq):

        # 0 : insert
        if opt == 0:
            b = checker_insert(A, val)
            # print(opt, val, ans, b)
            if b != ans:
                return False

        # 1 : delete
        elif opt==1:
            b = checker_delete(A, val)
            # print(opt, val, ans, b)
            if b != ans:
                return False

        # 2 : select
        elif opt==2:
            b = checker_select(A, val)
            # print(opt, val, ans, b)
            if b != ans:
                return False

        # 3 : rank
        else:
            b = checker_rank(A, val)
            # print(opt, val, ans, b)
            if b != ans:
                return False

    return True

if __name__=="__main__":

    # 0 : insert
    # 1 : delete
    # 2 : select
    # 3 : rank

    # Test Case 1
    opt_seq = [ ]
    in_seq  = [ ]
    out_seq = [ ]

    # insert
    opt_seq.extend([ 0, 0, 0, 0, 0, 0])
    in_seq.extend([41, 38, 31, 12, 19, 8])

    # select
    opt_seq.extend([2])
    in_seq.extend([2])

    # delete
    opt_seq.extend([1])
    in_seq.extend([12])

    # select
    opt_seq.extend([2, 2])
    in_seq.extend([2, 50])

    # rank
    opt_seq.extend([3, 3, 3, 3])
    in_seq.extend([31, 8, 38, 5])

    # delete
    opt_seq.extend([1, 1, 1, 1])
    in_seq.extend([12, 51, 52, 53])

    # init tree global variables
    init()

    for opt, val in zip(opt_seq, in_seq):
        if opt == 0:
            out_seq.append(os_insert(val))
        elif opt == 1:
            out_seq.append(os_delete(val))
        elif opt == 2:
            out_seq.append(os_select(val))
        elif opt == 3:
            out_seq.append(os_rank(val))

    if check(opt_seq, in_seq, out_seq):
        print("correct")
    else:
        print("incorrect")

    #######################################################################################################################################

    # 0 : insert
    # 1 : delete
    # 2 : select
    # 3 : rank

    # Test Case 2
    opt_seq = [ ]
    in_seq  = [ ]
    out_seq = [ ]

    # select
    opt_seq.extend([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    in_seq.extend([4,5,6,7,8,9,12,13,14,15,16])

    # insert
    opt_seq.extend([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    in_seq.extend([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    # select
    opt_seq.extend([2, 2, 2, 2, 2])
    in_seq.extend([2, 4, 6, 8, 10])

    # rank
    opt_seq.extend([3, 3, 3, 3, 3])
    in_seq.extend([7,8,9,10,11])

    # delete
    opt_seq.extend([1, 1, 1, 1, 1, 1])
    in_seq.extend([1, 3, 5, 7, 9, 11])

    # select
    opt_seq.extend([2, 2, 2, 2])
    in_seq.extend([2, 4, 6, 8])

    # rank
    opt_seq.extend([3, 3, 3, 3])
    in_seq.extend([31, 8, 38, 5])

    # delete
    opt_seq.extend([1, 1, 1, 1])
    in_seq.extend([12, 51, 52, 53])

    # init tree global variables
    init()

    for opt, val in zip(opt_seq, in_seq):
        if opt == 0:
            out_seq.append(os_insert(val))
        elif opt == 1:
            out_seq.append(os_delete(val))
        elif opt == 2:
            out_seq.append(os_select(val))
        elif opt == 3:
            out_seq.append(os_rank(val))

    if check(opt_seq, in_seq, out_seq):
        print("correct")
    else:
        print("incorrect")

    #######################################################################################################################################

    # 0 : insert
    # 1 : delete
    # 2 : select
    # 3 : rank

    # Test Case 3
    opt_seq = []
    in_seq = []
    out_seq = []

    for i in range(30000):

        opt_seq = []
        in_seq = []
        out_seq = []

        for j in range(3000):

            # create random operation
            opt_seq.append(random.randint(0, 3))

            # create random number
            in_seq.append(random.randint(1, 9999))

        # init tree global variables
        init()

        for opt, val in zip(opt_seq, in_seq):
            if opt == 0:
                out_seq.append(os_insert(val))
            elif opt == 1:
                out_seq.append(os_delete(val))
            elif opt == 2:
                out_seq.append(os_select(val))
            elif opt == 3:
                out_seq.append(os_rank(val))

        if check(opt_seq, in_seq, out_seq):
            print(i, "correct")
        else:
            print(i, "incorrect")
            print((opt_seq, in_seq, out_seq))
            break