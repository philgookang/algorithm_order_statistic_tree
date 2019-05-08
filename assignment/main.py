from hw2 import *

if __name__=="__main__":
    
    #0 : insert
    #1 : delete
    #2 : select
    #3 : rank
    opt_seq = [ 0, 0, 0, 0, 0 ]
    in_seq = [ 1, 2, 3, 3, 1 ]
    out_seq = [ 1, 2, 3, 0, 1 ] #4th element 1 -> 0

    if check(opt_seq,in_seq,out_seq):
        print("correct")
    else:
        print("incorrect")    

    init()
    opt_seq = [ 0, 1, 0, 0, 2, 3 ]
    in_seq = [ 1, 1, 1, 2, 1, 2 ]
    out_seq = [ ]
    for opt,val in zip(opt_seq,in_seq):
        if opt==0:
            out_seq.append(os_insert(val))
        elif opt==1:
            out_seq.append(os_delete(val))
        elif opt==2:
            out_seq.append(os_select(val))
        elif opt==3:
            out_seq.append(os_rank(val))
    
    if check(opt_seq,in_seq,out_seq):
        print("correct")
    else:
        print("incorrect")    
