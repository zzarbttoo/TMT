# 1주차 1번_K번째 수
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for command in commands:
        ar1 = array[command[0]-1:command[1]]   # i부터 j까지 슬라이싱
        ar1.sort()   # 자른 후 정렬
        answer.append(ar1[command[2]-1])   # k번째 수(인덱스는 k-1) 배열에 담기
    return answer

print(solution(array, commands))