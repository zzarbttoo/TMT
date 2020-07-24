def prime(x) :
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

import itertools

def solution(num):
    answer = 0
    a=[]
    for i in range(1,len(num)+1) :
        a.extend(list(map(''.join, itertools.permutations(num, i))))
    for k in range(len(a)):
        a[k]=int(a[k])
    a=list(set(a))
    for j in a :
        if prime(j):
            answer+=1
    return answer
