import itertools as itt

def check_stbl(num,base) :
    num=list(num)
    val=list(str(base[0]))
    st=0
    bl=0
    for i in range(3) :
        if num[i]==val[i]:
            st+=1
        elif num[i] in val:
            bl+=1
    if st==base[1] and bl==base[2]:
        return True
    else:
        return False

def solution(baseball):
    answer = 0
    num=[]
    for i in range(1,10):
        num.append(str(i))
    num=list(map(''.join, itt.permutations(num,3)))
    for base in baseball :
        rv=[]
        for temp in num :
            if not check_stbl(temp,base) :
                rv.append(temp)
        for r in rv:
            num.remove(r)
    answer=len(num)
    return answer
