# #내 풀이

# def solution(s):
#     answer=  0
#     answer_lang = ""
#     temp_num = 0 #indexing clicing 값
#     temp1 = 0 #갯수
#     temp2 = "" #슬라이스한 문자
#     hash = {}

#     if len(s) == 1: return 1
    
#     for i in range (1, len(s)):
        
#         while(True):
            
#             if(temp_num  > len(s) - 1): break
#             if(temp_num + i <= len(s)):
#                 if(s[temp_num:temp_num + i] == s[temp_num + i: temp_num+ 2*i]):
#                     temp1 +=1
#                     temp2 = s[temp_num : temp_num + i]
#                 else:
#                     temp1 += 1
#                     temp2 = s[temp_num : temp_num + i]
#                     if(temp1 !=1):
#                         answer_lang += str(temp1)
#                     answer_lang += temp2
#                     temp1 = 0
#                     temp2 = "" 
#             else:
#                 temp1 = 1
#                 temp2 = s[temp_num :len(s)]
#                 answer_lang += temp2

#             temp_num += i

#         hash[i] = hash.get(i, len(answer_lang))
#         answer_lang = ""
#         temp1 = 0
#         temp2 = ""
#         temp_num = 0

#     return min(hash.values())
            



# 강의 풀이
# 1 이상 10000 이하로 시간 복잡도 O(N^2)으로 해결해야한다

def solution(s):

    answer = len(s)

    #1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)):
        compressed= ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j : j + step]
                count += 1
        compressed += str(count) + prev if count >=2 else prev
        answer = min(answer, len(compressed))
    return answer





# 슬라이싱 https://twpower.github.io/119-python-list-slicing-examples














print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede")) #8
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd")) #17


#문자열 concat https://118k.tistory.com/447



