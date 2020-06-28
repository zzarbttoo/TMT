
# # 풀이 1 : 원래 이렇게 하려고 했는데 실패(너무 슬퍼하는 편)
def solution(numbers):

    answer = ""
    count = 0

    numbersSorted = sorted(numbers, key = lambda x :(x/pow(10,len(str(x)))), reverse = True)

    # print(numbersSorted)

    if(len(numbersSorted) == 0):
         return "0" 
    
    # for i in numbersSorted:
    #     print(i ,(int) (i/pow(10, len(str(i)) * 10)))
        
    

    for i in numbersSorted:
        
    
        
        if(count == 0 and i == 0):
            answer = "0"
            break
   
        

        answer += str(i)
        count += 1

    return answer

#파이썬 문자열 합치기
# https://www.pymoon.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%95%A9%EC%B9%98%EA%B8%B0
#순열(permutation)을 쓸 수는 있지만, 
#lambda 값을 이용해 sort를 진행한다 : https://dailyheumsi.tistory.com/67
#해쉬를 쓰면 빨라질 수 있나 생각해본다(생각만)
#이중 조건을 사용해본다 (lambda) : https://soooprmx.tistory.com/entry/%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%A0%AC%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95


#solution2 
# def solution(numbers):

#     answer= ""
#     temp = []
#     count = 0

#     for i in number:

#         if()

#         count+=1



#     return answer

# numbers1=[6, 10, 2] #6 2 10
# numbers2 =[3, 30, 34, 5, 9] # 9 5 3 34 30
# numbers3 = [1, 10, 2, 20] # 2 20 1 10 이렇게 sorting 해야한다 
# numbers4 = [0, 0, 0, 0, 0]
# numbers5 = [6, 646, 5]
numbers6 = []

# print(solution(numbers1))
# print(solution(numbers2))
# print(solution(numbers3))
# print(solution(numbers4))
# print(solution(numbers5))
print(solution(numbers6))


#다른 사람 풀이
# def solution(numbers):
# answer = ''
# numbers = list(map(str,numbers))
# numbers.sort(key = lambda x:x*3,reverse=True)
# for i in numbers:
# answer+=i
# return answer