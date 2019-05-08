def init():
    global l
    global cnt
    l = []

def os_insert(x):
    if x in l:
        return 0
    else:
        l.append(x)
        return x

def os_delete(x):
    if x in l:
        l.remove(x)
        return x
    else:
        return 0

def os_select(i):
    l.sort()
    if i-1 < len(l):
        return l[i-1]
    else:
        return 0

def os_rank(x):
    l.sort()
    if x in l:
        for e,order in zip(l,range(len(l))):
            if e == x:
                return order + 1
    else:
        return 0

def check(opt_seq,in_seq,out_seq):
    init()
    for opt,val,ans in zip(opt_seq,in_seq,out_seq):
        if opt==0:
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
