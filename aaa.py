import random

def insert(array, val):
    if val in array:
        return 0
    array.append(val)
    return val

def delete(array, val):
    if val in array:
        array.remove(val)
        return val
    return 0

# CLRS textbook partition pseudocode
# page: 147
def Partition(A, p, r):
    x = A[r]    # select pivot as the last element in list
    i = p - 1   # get starting position
    for j in range(p, r):
        if A[j] <= x:    # check current value is smaller than pivot
            i = i + 1
            A[i], A[j] =  A[j], A[i]    # switch location
    A[i + 1], A[r] = A[r], A[i + 1]     # move pivot to correct location
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
        return RandomSelect(A, p, q-1, i)
    else:
        return RandomSelect(A, q + 1, r, i - k)

def findRank(A, x):
    location = 0
    A.sort()
    for ind,val in enumerate(A):
        if x == A[ind]:
            location = ind
            break
    return location + 1


if __name__ == "__main__":
    A = []

    print('I', insert(A, 41))
    print('I', insert(A, 38))
    print('I', insert(A, 31))
    print('I', insert(A, 12))
    print('I', insert(A, 19))
    print('I', insert(A, 8))

    print('S', RandomSelect(A.copy(), 0, (len(A) - 1), 5))
    print('S', RandomSelect(A.copy(), 0, (len(A) - 1), 3))
    print('S', RandomSelect(A.copy(), 0, (len(A) - 1), 2))
    print('S', RandomSelect(A.copy(), 0, (len(A) - 1), 4))
    print('S', RandomSelect(A.copy(), 0, (len(A) - 1), 1))

    print('R', findRank(A.copy(), 41))
    print('R', findRank(A.copy(), 38))
    print('R', findRank(A.copy(), 31))
    print('R', findRank(A.copy(), 12))
    print('R', findRank(A.copy(), 19))
    print('R', findRank(A.copy(), 8))
