#이렇게 풀면 폭망할 거 같다^^
# def seperate(p):

#     u = ""
#     v = ""

#     currPlace = 0
#     stack = []

#     if(p[0] == "("):
#         for i in range(0, len(p)):
#             if p[i] == "(":
#                 stack.append("(")
#             elif p[i] == ")":
#                     stack.pop()
#             currPlace+=1
#             if(len(stack)==0):
#                 break

                   
#     elif(p[0] == ")"):
#         for i in range(0, len(p)):
#             if p[i] == ")":
#                 stack.append(")")
#             elif p[i] == "(":
#                 stack.pop()
#             currPlace+=1
#             if(len(stack)==0):
#                 break
    
#     u = p[0 : currPlace]
#     v = p[currPlace:len(p)]

#     return u, v


# def isUTrash(u, v):

#     isTrash = False
#     stack = []

#     #True 조건이 제대로 걸렸는지 디버깅 해보기

#     if len(u)== 0 and len(v) != 0:
#         isTrash = True
#     for i in range(0, len(u)):
#         if u[i] == "(":
#             stack.extend(u[i])
#         elif u[i] == ")":
#             if stack:
#                 stack.pop()
#             else:
#                 isTrash = True
#                 break

#     if len(stack) != 0 :
#         isTrash = True
#     return isTrash
        


# def UTrashCleaner(u, v):

#     u = u[1:len(u)-1]
#     u1 = ""
#     for i in range(0, len(u)):
#         if(u[i] == "("):
#             u1+=")"
#         elif(u[i] == ")"):
#             u1+="("
    
#     u = "(" + v + ")" + u1
#     v = ""

#     return u, v



# def solution(p):

#     u = ""
#     v = "" 
#     u1 = ""
#     u2 = ""

#     u, v = seperate(p)
#     while(True):
        

#         if(isUTrash(u, v)):
#             u, v = UTrashCleaner(u,v)
        
#         if(v == ""):
#             break
#         else:
#             u1, v1 = seperate(v)
           
#             if(isUTrash(u1,v1)):
#                 u1, v1 = UTrashCleaner(u1, v1)
            
#             u = u + u1
#             v = v1

#             break

#     return u

#programmers 풀이

def balanced_index(p):
    count = 0

    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1

    return True


def solution(p):
    answer = ''

    if p == '':
        return answer
    index = balanced_index(p)

    u= p[:index + 1]
    v =p[index +1 : ]

    if check_proper(u):
        #recursive
        answer = u + solution(v)
    else:
        answer = "("
        #recursive
        answer += solution(v)
        answer += ")"
        #slicing index
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer

p1 = "(()())()"
p2 = ")("
p3 = "()))((()"

print(solution(p1))
print(solution(p2))
print(solution(p3))

            



    







    


