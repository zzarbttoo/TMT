def solution(s):
    answer=  0
    answer_lang = ""
    temp_num = 0 #indexing clicing 값
    temp1 = 0 #갯수
    temp2 = "" #슬라이스한 문자
    hash = {}

    
    for i in range (1, len(s)):
        
        while(True):
            
            if(temp_num  > len(s) - 1): break
            if(temp_num + i <= len(s)):
                if(s[temp_num:temp_num + i] == s[temp_num + i: temp_num+ 2*i]):
                    temp1 +=1
                    temp2 = s[temp_num : temp_num + i]
                else:
                    temp1 += 1
                    temp2 = s[temp_num : temp_num + i]
                    if(temp1 !=1):
                        answer_lang += str(temp1)
                    answer_lang += temp2
                    temp1 = 0
                    temp2 = "" 
            else:
                temp1 = 1
                temp2 = s[temp_num :len(s)]
                answer_lang += temp2

            temp_num += i

        hash[i] = hash.get(i, len(answer_lang))
        answer_lang = ""
        temp1 = 0
        temp2 = ""
        temp_num = 0

    return min(hash.values())
            

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede")) #8
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd")) #17


#문자열 concat https://118k.tistory.com/447