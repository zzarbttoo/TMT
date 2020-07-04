def seperate(p):

    u = ""
    v = ""

    sum1 = 0
    sum2 = 0
    currPlace = 0
    stack = []

    for i in range (0 , len(p)):
        if p[currPlace] == "(" :
            stack.append("(")
        elif p[currPlace] == ")":
            if stack:
                stack.pop()
            else:
                break
        currPlace+=1
    
    u = p[0 : currPlace]
    v = p[currPlace:len(p)]

    return u, v


def isUTrash(u, v):

    isTrash = False
    stack = []

    #True 조건이 제대로 걸렸는지 디버깅 해보기

    if len(u)== 0 and len(v) != 0:
        isTrash = True
    for i in range(0, len(u)):
        if u[i] == "(":
            stack.extend=u[i]
        elif u[i] == ")":
            if stack is not None:
                stack.pop()
            else:
                isTrash = True

    if len(stack) != 0 :
        isTrash = True
    return isTrash
        


def UTrashCleaner(u, v):

    u = u[1:len(u)]
    for i in range(0, len(u)):
        if(u[i] == "("):
            u[i] == ")"
        elif(u[i] == ")"):
            u[i] == "("
    
    u = "(" + v + ")" + u
    v = ""

    return u, v



def solution(p):

    u = ""
    v = "" 
    u1 = ""
    u2 = ""

    u, v = seperate(p)
    while(True):
        
        if(v == ""):
            break

        if(isUTrash(u, v)):
            u, v = UTrashCleaner(u,v)
        
        else:
            u1, v1 = seperate(v)
            
            u = u + u1
            v = v1

    return u



p1 = "(()())()"
p2 = ")("
p3 = "()))((()"

# print(solution(p1))
print(solution(p2))
# print(solution(p3))

            



    







    


