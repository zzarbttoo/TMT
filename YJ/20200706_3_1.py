#효율성 통과 못한 풀이
# from collections import deque

# def solution(prices):
#     answer=[]

#     for i in range(0, len(prices)):

#         sum = 0 
#         queue = deque(prices[i+1:len(prices)])

#         while(queue):

#             sum += 1
#             if(prices[i] > queue.popleft()):
#                 break
        
#         answer.append(sum)
   
#     return answer

#     리스트 슬라이싱을 매번 해서 실행 시간이 많이 증가했다고 생각합니다. python document를 참고하면 리스트 슬라이싱은 O(k) ... (k는 잘라낸 리스트의 크기) 가 소요됩니다.
# 다른 코드는 아마 indexing만 이용해서 i+1에서 시작했을 겁니다. 분명 Python에서 for i in range(3, len(prices)) 같은 c style code를 가급적 안쓰는 게 좋지만, 지금처럼 실행 속도 차이가 클 때는 써줘야 합니다.
# range 내장함수 사용법을 참고 바랍니다.
# (추가)
# 이중 for문은 O(n2 ) 라서 가능한 사용하지 않아야 합니다. 이 문제는 이중 for문을 사용하지 않고 조금 더 효율적으로 푸는 방법이 있다는 점 참고 바랍니다.

#내풀이
def solution(prices): 
    answer = []

    for i, price in enumerate(prices):
        sum =0
        for j in range(i+1, len(prices)):
            sum += 1
            if(prices[i] > prices[j]):
                break
        answer.append(sum)
        
    return answer 


# 4 3 1 1 0
print(solution([1,2,3,2,3]))
